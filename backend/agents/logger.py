from langgraph.graph import END
from langgraph.types import Command 
import json

from db.crud import save_request
from pydantic_classes import RequestState

def logger(state: RequestState):
    save_request(
        request=state["request"],

        classification=state["classification"].classification,
        urgency=state["urgency"],
        highPriority=state["highPriority"],

        assigned_team=state["assigned_team"],
        generated_response=state["response"],
        follow_up=state["follow_up"],
        status=state["status"],

        reasoning=state["classification"].reasoning,
        confidence=state["classification"].confidence,

        service_type=state.get("service_type"),
        service_details=state.get("service_details"),

        escalation_reason=state.get("escalation_reason"),

        actions_taken=json.dumps(
            state.get("actions_taken", [])
        )
    )

    return Command(goto=END)