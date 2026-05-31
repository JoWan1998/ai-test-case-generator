# 🧪 AI Test Case Generator

> Genera casos de prueba automáticamente usando LLMs.
> Powered by Groq API. 100% gratuito y open source.

## 🚀 Demo en vivo
- [ai-test-case-generator-jose-wannan.streamlit.app](https://ai-test-case-generator-jose-wannan.streamlit.app/)
---

## 📋 What it does

Paste a feature description or user story, choose a language and output format, and get **5 ready-to-use functional test cases** in seconds:

- ✅ 2 Happy Path scenarios
- ❌ 2 Negative scenarios
- ⚠️ 1 Edge Case / Boundary scenario

Each case includes title, priority, severity, preconditions, atomic steps, expected results, and concrete test data — no placeholders.
---

## 🛠️ Tech Stack

- **[Groq API](https://console.groq.com)** — Free LLM inference (Llama 3, Qwen3)
- **[Streamlit](https://streamlit.io)** — Web UI, no frontend needed
- **[Python](https://python.org)** — Core language
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Secure API key management
---

## ⚡ Run locally

### 1. Clone the repo

```bash
git clone https://github.com/JoWan1998/ai-test-case-generator
cd ai-test-case-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Get a free API key at [console.groq.com](https://console.groq.com) — no credit card required.

```bash
# Create a .env file (never commit this)
cp .env.example .env
```

Open `.env` and add your key:

```
GROQ_API_KEY=gsk_your_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`

---

## 📁 Project Structure

```
ai-test-case-generator/
├── app.py              # Streamlit UI — main entry point
├── generator.py        # Groq API connection and LLM call
├── prompts.py          # System prompts, format templates, language config
├── requirements.txt    # Direct dependencies only
├── .env.example        # API key template (safe to commit)
├── .gitignore          # Excludes .env and venv
└── README.md
```
---

## 👤 Author

**José Orlando Wannan Escobar**
QA Automation Engineer · AI Master's Student
[LinkedIn](https://linkedin.com/in/josewannan1998) · [GitHub](https://github.com/JoWan1998)

---

## 📄 License

[MIT](LICENSE) — free to use, modify and distribute.
