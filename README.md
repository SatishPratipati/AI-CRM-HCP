# AI First CRM - HCP Module

## Project Overview

AI First CRM - HCP Module is an AI-powered Customer Relationship Management (CRM) application designed for pharmaceutical field representatives to manage Healthcare Professional (HCP) interactions.

The application provides two methods for logging interactions:

- Structured Interaction Form
- AI-powered Conversational Assistant

The AI Assistant is powered by **LangGraph** and **Groq LLM**, which generates summaries and recommendations from natural language conversations.

---

# Features

- Log HCP interactions using a structured form
- AI-powered conversational interface
- AI-generated interaction summaries
- View interaction history
- Search previous HCP interactions
- Edit interaction details
- Recommend next sales actions
- Responsive dashboard UI

---

# Technology Stack

## Frontend

- React
- Redux Toolkit
- Axios
- CSS
- Google Inter Font

## Backend

- FastAPI
- Python
- LangGraph
- Groq LLM (Llama-3.3-70B-Versatile)
- SQLAlchemy

## Database

- MySQL

---

# LangGraph AI Agent

The LangGraph agent manages HCP interactions using the following tools:

1. Log Interaction
2. Edit Interaction
3. Search HCP
4. Summarize Interactions
5. Recommend Next Action

The agent processes natural language input, generates summaries using Groq LLM, stores interactions in MySQL, and returns AI-generated responses to the React application.

---

# Project Structure

```
AI-CRM-HCP
│
├── Backend
│   ├── app
│   ├── requirements.txt
│   └── ...
│
├── Frontend
│   ├── src
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/SatishPratipati/AI-CRM-HCP.git
```

---

## 2. Backend Setup

```bash
cd Backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

```bash
cd Frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# AI Workflow

1. User enters interaction details using the form or AI Assistant.
2. FastAPI sends the request to the LangGraph agent.
3. LangGraph invokes the Groq LLM.
4. The LLM generates a summary or recommendation.
5. The interaction is stored in the MySQL database.
6. The AI response is displayed in the React application.

---

# Future Enhancements

- User Authentication
- Role-Based Access Control
- Voice-based Interaction Logging
- Calendar Integration
- Analytics Dashboard
- Email Notifications

---

# Author

**Satish Prathipati**
