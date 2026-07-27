import os

from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_core.prompts import PromptTemplate


load_dotenv()



def cargar_base_conocimiento():

    embeddings = CohereEmbeddings(
        model="embed-multilingual-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )


    memoria_documental = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )


    return memoria_documental



def preguntar_documento(pregunta):

    memoria = cargar_base_conocimiento()


    resultados = memoria.similarity_search_with_score(
        pregunta,
        k=5
    )


    contenidos = []

    for documento, puntuacion in resultados:
        contenidos.append(documento)


    contexto = "\n\n".join(
        contenido.page_content
        for contenido in contenidos
    )


    plantilla = PromptTemplate(
        template="""

Eres Smart Document Assistant, un asistente virtual para consultar documentos.

Normas:
- Responde solamente con información del documento.
- Prioriza respuestas precisas y fáciles de entender.
- No inventes información.
- Si no existe información suficiente responde:
"No encuentro esa información en el documento."

INFORMACIÓN DISPONIBLE:
{contexto}

PREGUNTA DEL USUARIO:
{pregunta}

RESPUESTA:
""",
        input_variables=[
            "contexto",
            "pregunta"
        ]
    )


    modelo = ChatCohere(
        model="command-r-plus-08-2024",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )


    respuesta = modelo.invoke(
        plantilla.format(
            contexto=contexto,
            pregunta=pregunta
        )
    )


    return respuesta.content
