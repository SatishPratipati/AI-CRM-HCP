from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.groq_client import llm
from app.tools import (
    log_interaction,
    edit_interaction,
    search_hcp,
    summarize_interactions,
    recommend_next_action,
)


class AgentState(TypedDict):
    message: str
    response: str


def router(state: AgentState):

    message = state["message"].lower()

    if "edit" in message:

        response = edit_interaction.invoke(
            {
                "interaction_id": 1,
                "follow_up": "Tomorrow",
            }
        )

    elif "search" in message:

        response = search_hcp.invoke(
            {
                "hcp_name": "Dr",
            }
        )

    elif "summary" in message:

        response = summarize_interactions.invoke({})

    elif "recommend" in message:

        response = recommend_next_action.invoke(
            {
                "doctor_name": "Dr Sharma",
            }
        )

    else:

        summary = llm.invoke(
            f"""
Summarize this HCP interaction in one sentence.

Interaction:
{message}
"""
        ).content

        log_interaction.invoke(
            {
                "hcp_name": "Unknown",
                "hospital": "Unknown",
                "specialization": "General",
                "discussion": message,
                "summary": summary,
                "follow_up": "Next Visit",
            }
        )

        response = summary

    return {
        "message": state["message"],
        "response": str(response),
    }


builder = StateGraph(AgentState)

builder.add_node("router", router)

builder.set_entry_point("router")

builder.add_edge("router", END)

crm_agent = builder.compile()