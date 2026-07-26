from pydantic import BaseModel
from enum import Enum

class ApiRequestBody(BaseModel):
    request: str


class ApiResponseBody(BaseModel):
    classification: str
    urgency: str
    response: str

    assigned_team: str
    status: str
    follow_up: str

    highPriority: bool


class DashboardType(str, Enum):
    complaint = "complaint"
    enquiry = "enquiry"
    service = "service"
    escalation = "escalation"