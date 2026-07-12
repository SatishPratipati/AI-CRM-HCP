from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(100))
    hospital = Column(String(150))
    specialization = Column(String(100))

    discussion = Column(String(1000))
    summary = Column(String(1000))

    follow_up = Column(String(100))

    created_at = Column(DateTime, default=datetime.utcnow)