from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Interaction
from app.schemas import InteractionCreate, InteractionUpdate

router = APIRouter(prefix="/interactions", tags=["Interactions"])


@router.post("/")
def create_interaction(data: InteractionCreate, db: Session = Depends(get_db)):
    interaction = Interaction(
        hcp_name=data.hcp_name,
        hospital=data.hospital,
        specialization=data.specialization,
        discussion=data.discussion,
        summary=data.discussion,
        follow_up=data.follow_up
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


@router.get("/")
def get_interactions(db: Session = Depends(get_db)):
    return db.query(Interaction).all()


@router.put("/{interaction_id}")
def update_interaction(
    interaction_id: int,
    data: InteractionUpdate,
    db: Session = Depends(get_db),
):
    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")

    interaction.hcp_name = data.hcp_name
    interaction.hospital = data.hospital
    interaction.specialization = data.specialization
    interaction.discussion = data.discussion
    interaction.summary = data.discussion
    interaction.follow_up = data.follow_up

    db.commit()
    db.refresh(interaction)

    return interaction