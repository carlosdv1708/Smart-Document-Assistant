import streamlit as st

from src.loader import PDFLoader
from src.embeddings import crear_vectorstore
from src.chatbot import preguntar_documento


st.set_page_config(
    page_title="Smart Document Assistant",
    page_icon="📚"
)


st.title(
    "📚 Smart Document Assistant"
)


st.write(
    "Tu asistente personal para consultar información dentro de documentos PDF."
)


st.divider()


archivo = st.file_uploader(
    "📥 Cargar documento",
    type=["pdf"]
)


if archivo:

    ruta = "data/documento.pdf"


    with open(
        ruta,
        "wb"
    ) as f:

        f.write(
            archivo.getbuffer()
        )


    boton = st.button(
        "⚡ Procesar documento"
    )


    if boton:

        with st.spinner(
            "Creando base de conocimiento..."
        ):


            loader = PDFLoader(
                ruta
            )


            contenido = loader.extraer_texto()


            crear_vectorstore(
                contenido
            )


        st.session_state["activo"] = True


        st.success(
            "Documento aprendido correctamente"
        )



if st.session_state.get(
    "activo",
    False
):


    st.subheader(
        "🤔 Pregúntame sobre el documento"
    )


    pregunta = st.chat_input(
        "Escribe una pregunta..."
    )


    if pregunta:


        with st.spinner(
            "Pensando..."
        ):


            respuesta = preguntar_documento(
                pregunta
            )


        with st.chat_message(
            "assistant"
        ):

            st.write(
                respuesta
            )