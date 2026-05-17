
# 🏋️ AI Fitness Chatbot

A local, privacy-focused AI chatbot that suggests fitness workouts using natural language queries. The system uses a local LLM (Mistral via Ollama), TF-IDF vectorization, and FAISS for fast similarity search — all running entirely offline.

---

## 🚀 Overview

This chatbot is designed to understand user fitness queries like:
> _"Suggest me a workout for back and biceps"_

It then finds the most relevant exercises from a CSV dataset, builds a natural language prompt, and uses Mistral (running locally with Ollama) to generate a conversational response.

---

## 🧠 Technologies Used

| Component | Tech Used |
|----------|------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python) |
| **Vectorization** | `TfidfVectorizer` from scikit-learn |
| **Similarity Search** | FAISS (`faiss-cpu`) |
| **Local LLM** | Mistral via Ollama (`ollama run mistral`) |
| **Data Source** | CSV file with structured exercise data |

---

## 📦 Installation & Usage

### 1. Install Backend Dependencies

```bash
pip install flask pandas scikit-learn faiss-cpu flask-cors
```

### 2. Download and Run Mistral Model (via Ollama)

Make sure you have [Ollama](https://ollama.com/) installed.

```bash
ollama run mistral
```

Ensure Mistral is downloaded and running locally before launching the Flask API.

### 3. Start the Flask Server

```bash
python app.py
```

Flask will start at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### 4. Open the Frontend

Simply open `index.html` in any modern browser (no web server required for local testing).

---

flowchart TD
    A["🧍 User<br>Types fitness query"] --> B["💻 HTML/JS Frontend<br>Captures input"]
    B --> C["📡 Sends POST to Flask API"]
    C --> D["🌐 Flask Server<br>Receives the request"]
    D --> E["🧠 Vectorizer<br>Converts input via TF-IDF"]
    E --> F["🔍 FAISS Index<br>Search top 5 relevant exercises"]
    F --> G["📂 CSV Dataset<br>Returns exercise rows"]
    G --> H["🧾 Prompt Builder<br>Context + Question"]
    H --> I["🤖 Mistral LLM via Ollama<br>Generates answer"]
    I --> J["📨 LLM Output<br>Raw response"]
    J --> K["🧰 Flask API<br>Formats JSON"]
    K --> L["🖥️ Frontend Receives JSON"]
    L --> M["💬 Chat UI<br>Displays bot response"]

    %% Styling
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#00f,color:#fff,stroke-width:2px
    style F fill:#00ff00,stroke:#333

---

## 🤝 Credits

Built with ❤️ using local-first AI tools like Ollama and FAISS.
