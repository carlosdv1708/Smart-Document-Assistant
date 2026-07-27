from pypdf import PdfReader
import re


class PDFLoader:

    def __init__(self, ruta_pdf):
        self.ruta_pdf = ruta_pdf


    def extraer_texto(self):

        lector = PdfReader(self.ruta_pdf)

        texto = ""

        for pagina in lector.pages:

            contenido = pagina.extract_text()

            if contenido:
                texto += contenido + "\n"


        texto = self.limpiar_texto(texto)

        return texto



    def limpiar_texto(self, texto):

        texto = texto.replace("\n", " ")

        texto = re.sub(
            r"\s+",
            " ",
            texto
        )

        return texto.strip()