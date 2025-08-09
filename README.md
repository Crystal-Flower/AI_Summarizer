# 📝 AI Summarizer – PDF & Text Summarization with Ollama & Streamlit

**Instantly summarize PDFs (up to 10 pages) or plain text** using local AI models powered by [Ollama](https://ollama.com/) — all through a clean and interactive [Streamlit](https://streamlit.io/) interface.

## 🚀 Features

* **PDF Summarization** – Upload a PDF, automatically extract text, and get concise bullet-point summaries.
* **Text Summarization** – Paste text directly into the app and summarize instantly.
* **Multiple AI Models** – Choose from available Ollama models installed locally.
* **Fast & Local** – Runs entirely on your machine (no external API calls).
* **Simple UI** – User-friendly tabs for PDF and text input.

## 🛠 Tech Stack

* **Python** – Core logic and backend
* **Streamlit** – Interactive web interface
* **pypdf** – PDF text extraction
* **Ollama** – Local LLM inference
* **Requests** – API communication with Ollama

## 📂 How It Works

1. **Load available Ollama models** – Automatically lists installed models.
2. **Upload PDF / Enter Text** – Choose your preferred input method.
3. **Summarization** – The app sends the extracted text to the chosen Ollama model with a summarization prompt.
4. **Results** – Receive a clean, concise summary in bullet points.

## ▶️ Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-summarizer.git
```

### 2️⃣ Install dependencies

```bash
pip install streamlit pypdf requests ollama
```

### 3️⃣ Make sure Ollama is running locally

[Download Ollama](https://ollama.com/download) and run:

```bash
ollama serve
```

You can also pull models like:

```bash
ollama pull llama3.2
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run main.py
```

## 💡 Example Use Cases

* Quickly summarizing research papers
* Condensing long reports for meetings
* Extracting key points from technical documents

## 📸 Screenshot
![Image](https://github.com/Crystal-Flower/AI_Summarizer/blob/main/Screenshot%202025-08-09%20230757.png?raw=true)
![Image](https://github.com/Crystal-Flower/AI_Summarizer/blob/main/Screenshot%202025-08-09%20231041.png?raw=true)

---

💬 **Let's Connect!**
If you like this project or want to collaborate, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/anandhappriya-s-b46697343/).

