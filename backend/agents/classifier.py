from langgraph.types import Command 
from typing import Literal
from langgraph.graph import END

from pydantic_classes import RequestState, Classification
from configs import llm
from configs import routes

def classifier(state: RequestState) -> Command[Literal["complaint", "enquiry", "service", "escalation"]]:
    system_prompt = """
    You are an AI request classification agent.

    Your ONLY task is to analyze the user's request.

    Return:

    1. classification
    Complaint:
    - User expresses dissatisfaction.
    - Reports a bad experience.
    - Reports a defective product or poor service.

    General Enquiry:
    - User is asking for information.

    Service Request:
    - User wants something done.

    Escalation:
    - Serious issue requiring immediate attention.
    - Legal threat.
    - Data breach.
    - Fraud.
    - Manager complaint.

    2. confidence
    Between 0 and 1.

    3. reasoning
    One sentence explaining why.

    Do not generate responses for the customer.
    Do not solve the request.
    Only classify.
    """

    user_query = state["request"]
    if not user_query:
        return Command(
        update={
            "response": "Please provide a request."
        },
        goto=END
    )

    messages = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":user_query}
    ]

    response = llm.with_structured_output(Classification).invoke(messages)

    urgency_map = {
        "Complaint": "High",
        "General Enquiry": "Low",
        "Service Request": "Medium",
        "Escalation": "Critical",
    }
    urgency = urgency_map[response.classification]
    
    return Command(
        update={
            "classification": response,
            "urgency":urgency  
        },
        goto = routes[response.classification]
    )