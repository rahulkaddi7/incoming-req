from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean
from sqlalchemy.sql import func

from db.database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)

    request = Column(Text, nullable=False)

    classification = Column(String, nullable=False)
    urgency = Column(String, nullable=False)
    highPriority = Column(Boolean, default=False)

    assigned_team = Column(String)
    generated_response = Column(Text)
    follow_up = Column(String)
    status = Column(String)
    reasoning = Column(Text)
    confidence = Column(Float)

    service_type = Column(String)
    service_details = Column(Text)

    escalation_reason = Column(Text)

    actions_taken = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )