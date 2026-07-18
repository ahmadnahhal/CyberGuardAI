# CyberGuard AI

## Description

CyberGuard AI is an AI-powered cybersecurity assistant designed to help users analyze security risks, understand threats, and improve their cybersecurity awareness.

The system provides:

* Password analysis
* Secure password generation
* Phishing attempt detection
* AI-powered cybersecurity assistance
* Incident creation and tracking
* Report generation

## Features

### AI Cybersecurity Assistant

Users can ask cybersecurity-related questions and receive intelligent explanations and recommendations.

### Phishing Analyzer

Analyzes suspicious messages and identifies potential phishing indicators.

### Password Security Tools

Evaluates password strength and provides recommendations for creating stronger passwords.

### Incident Management

Stores and reviews cybersecurity incidents using a local database.

### Reports

Generates security reports based on analyzed incidents.

---

# Installation

## Requirements

* Python 3.x
* Docker (optional)
* A Groq API key for AI functionality

---

## Run Locally

1. Clone the repository:

```bash
git clone <repository-link>
cd CyberGuard-AI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create an environment file:

Copy `.env.example` and rename it to `.env`.

Example:

```bash
cp .env.example .env
```

4. Add your API key inside `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

5. Run the application:

```bash
streamlit run app.py
```

---

# Run with Docker

1. Create a `.env` file using the same steps above.

2. Build and start the application:

```bash
docker compose up --build
```

The application will then be available through the Streamlit interface.

---

# Technologies

* Python
* Streamlit
* LangGraph
* Groq API
* SQLite
* Docker

---

# Project Structure

```
CyberGuard-AI/
│
├── app/
│   ├── agent/
│   ├── database/
│   ├── tools/
│   ├── ui/
│   └── services/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# Security Notes

* Do not upload your `.env` file or API keys to GitHub.
* Use `.env.example` as a template for required environment variables.
