from langchain_core.tools import tool
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Interaction


@tool
def log_interaction(
    hcp_name: str,
    hospital: str,
    specialization: str,
    discussion: str,
    summary: str,
    follow_up: str,
) -> str:
    """
    Log a new HCP interaction into the CRM.
    """

    db: Session = SessionLocal()

    try:
        interaction = Interaction(
            hcp_name=hcp_name,
            hospital=hospital,
            specialization=specialization,
            discussion=discussion,
            summary=summary,
            follow_up=follow_up,
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return f"Interaction logged successfully. ID = {interaction.id}"

    finally:
        db.close()


@tool
def edit_interaction(
    interaction_id: int,
    follow_up: str,
) -> str:
    """
    Update follow-up date of an interaction.
    """

    db: Session = SessionLocal()

    try:

        interaction = (
            db.query(Interaction)
            .filter(Interaction.id == interaction_id)
            .first()
        )

        if interaction is None:
            return "Interaction not found."

        interaction.follow_up = follow_up

        db.commit()

        return "Interaction updated successfully."

    finally:
        db.close()


@tool
def search_hcp(
    hcp_name: str,
) -> str:
    """
    Search all interactions of an HCP.
    """

    db: Session = SessionLocal()

    try:

        interactions = (
            db.query(Interaction)
            .filter(Interaction.hcp_name.ilike(f"%{hcp_name}%"))
            .all()
        )

        if not interactions:
            return "No previous interactions found."

        output = []

        for item in interactions:

            output.append(
                f"""
Doctor : {item.hcp_name}
Hospital : {item.hospital}
Discussion : {item.summary}
Follow Up : {item.follow_up}
"""
            )

        return "\n".join(output)

    finally:
        db.close()


@tool
def summarize_interactions() -> str:
    """
    Return summaries of all logged interactions.
    """

    db: Session = SessionLocal()

    try:

        rows = db.query(Interaction).all()

        if not rows:
            return "No interactions available."

        return "\n".join(
            [f"{r.hcp_name}: {r.summary}" for r in rows]
        )

    finally:
        db.close()


@tool
def recommend_next_action(
    doctor_name: str,
) -> str:
    """
    Recommend the next sales action for an HCP.
    """

    return f"""
Recommended next actions for {doctor_name}

1. Schedule follow-up visit.
2. Share latest product brochure.
3. Provide product samples.
4. Record doctor's feedback.
5. Update CRM after visit.
"""