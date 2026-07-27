# 📚 Smart Document Assistant

Asistente virtual inteligente diseñado para consultar información dentro de documentos PDF mediante lenguaje natural.

El sistema utiliza inteligencia artificial para comprender el contenido del documento, recuperar información relevante y generar respuestas utilizando modelos de Cohere mediante una arquitectura **RAG (Retrieval Augmented Generation)**.

---

# ✨ Funcionalidades

- 📥 Carga de documentos PDF.
- 📖 Extracción automática de texto.
- 🧠 Creación de representaciones vectoriales.
- 🔍 Búsqueda inteligente de información mediante FAISS.
- 💬 Sistema de preguntas y respuestas.
- 🤖 Generación de respuestas con inteligencia artificial.
- 🌐 Interfaz interactiva desarrollada con Streamlit.

---

# 🏗 Arquitectura del sistema

```text
Documento PDF
      |
      ↓
Extractor de texto
      |
      ↓
Generación de embeddings
      |
      ↓
FAISS Vector Database
      |
      ↓
Consulta del usuario
      |
      ↓
Cohere AI
      |
      ↓
Respuesta generada
```

---

# 🛠 Tecnologías

| Tecnología | Función |
|---|---|
| Python | Desarrollo del agente |
| Streamlit | Interfaz gráfica web |
| Cohere | Modelo de inteligencia artificial |
| LangChain | Gestión del flujo RAG |
| FAISS | Recuperación semántica |
| PyPDF | Procesamiento de documentos PDF |

---

# ⚙ Instalación

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar al proyecto:

```bash
cd Smart-Document-Assistant
```

---

## 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Instalar librerías

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuración

Crear un archivo:

```text
.env
```

Agregar la clave de Cohere:

```env
COHERE_API_KEY=tu_api_key
```

---

# ▶ Ejecución

Iniciar la aplicación:

```bash
streamlit run app.py
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

---

# 💬 Ejemplos de uso

### Pregunta:

```text
Resume el contenido del documento.
```

### Respuesta:

```text
El agente analiza el documento y genera un resumen utilizando la información recuperada desde la fuente.
```

---

### Pregunta:

```text
¿Qué temas aparecen en el archivo?
```

### Respuesta:

```text
Los temas principales son identificados mediante el análisis semántico del contenido del documento.
```

---

# 📂 Organización del proyecto

```text
Smart-Document-Assistant
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
│
├── data
│   └── documento.pdf
│
└── src
    ├── loader.py
    ├── embeddings.py
    └── chatbot.py
```

---

# 👨‍💻 Autor

Creando un asistente documental basado en inteligencia artificial para la consulta de información mediante lenguaje natural.