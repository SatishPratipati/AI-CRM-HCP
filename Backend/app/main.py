from app.routers import ai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import interaction

app = FastAPI(
    title="AI First CRM - HCP Module",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interaction.router)
app.include_router(ai.router)


@app.get("/")
def home():
    return {"message": "AI First CRM Backend Running Successfully"}