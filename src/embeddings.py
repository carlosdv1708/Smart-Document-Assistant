import os

from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings


load_dotenv()


def crear_vectorstore(texto):

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300
)

    fragmentos = splitter.split_text(texto)


    embeddings = CohereEmbeddings(
        model="embed-multilingual-v3.0",
        cohere_api_key=os.getenv("COHERE_API_KEY")
    )


    vectorstore = FAISS.from_texts(
        fragmentos,
        embeddings
    )


    vectorstore.save_local(
        "vectorstore"
    )


    return vectorstore