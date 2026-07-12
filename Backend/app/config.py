import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/ai_crm"
)