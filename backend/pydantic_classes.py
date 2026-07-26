from typing import List, Literal, Literal
from pydantic import BaseModel
from langgraph.graph import MessagesState

class Classification(BaseModel):
    classification: Literal[
            "Complaint",
            "General Enquiry",
            "Service Request",
            "Escalation"
        ]
    confidence: float
    reasoning: str


class ServiceRequestResponse(BaseModel):
    service_type: str
    extracted_details: str
    assigned_department: str
    confirmation_message: str

    
class EscalationResponse(BaseModel):
    escalation_reason: str
    supervisor_team: str
    acknowledgement: str


class RequestState(MessagesState):
    request: str
    response: str
    
    urgency: str
    classification: Classification

    assigned_team: str
    follow_up: str
    status: str
    highPriority: bool

    service_type:str
    service_details: str

    escalation_reason: str

    actions_taken: List[str]
