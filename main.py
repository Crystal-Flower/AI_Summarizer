import streamlit as st
import requests
from pypdf import PdfReader
import ollama
import ollama
models = []
for i in ollama.list():
    for j in i[1]:
        models.append(j.model)
OLLAMA_URL = "http://localhost:11434/api/generate"

def read_pdf(file, max_pages=10):
    """Extracts text from PDF up to max_pages."""
    pdf = PdfReader(file)
    text = ""
    for page_num, page in enumerate(pdf.pages):
        if page_num >= max_pages:
            break
        text += page.extract_text() + "\n"
    return text.strip()

def summarize_text(text, model="llama3.2"):
    """Summarizes text using Ollama."""
    prompt = f"Summarize the following text in concise bullet points:\n\n{text}"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"Error: {e}"

# ---- Streamlit UI ----
st.set_page_config(page_title="AI Summarizer", page_icon="📝", layout="centered")
st.title("AI Summarizer")
st.markdown("Upload a PDF (up to 10 pages) **or** paste text directly, and get a summary.")

# Model selection
# model_choice = st.text_input("Ollama Model", value="llama2")
model_choice = st.selectbox("Ollama Model",models)
# Tabs for PDF and Text input
tab1, tab2 = st.tabs(["PDF Upload", "Text Input"])

with tab1:
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        with st.spinner("Reading PDF..."):
            pdf_text = read_pdf(uploaded_file)
        if pdf_text:
            st.success(f"Extracted text from PDF ({len(pdf_text.split())} words)")
            if st.button("Summarize PDF"):
                with st.spinner("Generating summary with Ollama..."):
                    summary = summarize_text(pdf_text, model_choice)
                    st.subheader("Summary")
                    st.write(summary)
        else:
            st.error("Could not extract text from PDF.")

with tab2:
    text_input = st.text_area("Enter text to summarize", height=200)
    if st.button("Summarize Text"):
        if 0 < text_input.strip() < 50000:
            with st.spinner("Generating summary with Ollama..."):
                summary = summarize_text(text_input, model_choice)
                st.subheader("Summary")
                st.write(summary)
        else:
            st.warning("Please enter some text first.")
