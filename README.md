# 🛡️ LLM Guardrails: Enterprise AI & Responsible AI
https://llm-guardrails-enterprise-ai-responsible.onrender.com

A full-stack implementation demonstrating **Defense-in-Depth Input and Output Guardrails** for Generative AI applications powered by **FastAPI** and **Google Gemini (google-genai)**.

---

## 🚀 Features

- **Input Guardrails**:
  - Type & empty input validation.
  - Length limitation (up to 5000 characters).
  - Blocked keyword detection (e.g., malware, exploit, weapon).
  - Prompt injection detection (e.g., "ignore previous instructions").
  - Jailbreak attempt detection (e.g., DAN mode, unrestricted mode).
- **Google Gemini Integration**:
  - Powered by the latest `google-genai` SDK and Gemini 2.5 Flash.
- **Output Guardrails**:
  - Empty response detection.
  - Sensitive information leakage prevention (e.g., API keys, passwords, private keys).
- **Interactive Web UI**:
  - Real-time pipeline visualizer (User $\rightarrow$ Input Guardrail $\rightarrow$ Gemini $\rightarrow$ Output Guardrail $\rightarrow$ Response).
  - Live security results dashboard displaying stage, category, and violation status.

---

## 🏗️ Architecture Pipeline

```
[User Prompt]
      │
      ▼
┌─────────────────────────┐
│ 1. Input Guardrail      │ ── Unsafe ──► [Block Request]
└─────────────────────────┘
      │ Safe
      ▼
┌─────────────────────────┐
│ 2. Gemini Model         │ ── Model Call
└─────────────────────────┘
      │ Response
      ▼
┌─────────────────────────┐
│ 3. Output Guardrail     │ ── Unsafe ──► [Block Response]
└─────────────────────────┘
      │ Safe
      ▼
[Safe Response to User]
```

---

## 🛠️ Project Structure

```
├── app.py                 # FastAPI application with endpoints
├── config.py              # Environment configuration & API key loading
├── gemini_service.py      # Google Gemini client & generation service
├── guardrails.py          # Input guardrail checks & regex patterns
├── output_guardrails.py   # Output guardrail validation
├── requirements.txt       # Project dependencies
├── templates/
│   └── index.html         # Frontend interface
└── static/
    ├── style.css          # Frontend stylesheet
    └── script.js          # Pipeline animation & API fetch logic
```

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ai-genai-agenticai-intelligence/LLM-Guardrails_-Enterprise-AI_-Responsible-AI.git
cd LLM-Guardrails_-Enterprise-AI_-Responsible-AI
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv myenv

# Windows (PowerShell)
.\myenv\Scripts\activate

# Linux / macOS
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory (or copy from `.env.example`):
```env
GEMINI_API_KEY="your_gemini_api_key_here"
GEMINI_MODEL="gemini-2.5-flash"
```

### 5. Run the Application
```bash
uvicorn app:app --reload
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📜 License
MIT License
