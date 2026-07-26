from sqlalchemy import func
from db.database import SessionLocal
from db.models import Request

def enquiry_dashboard():
    db = SessionLocal()

    try:
        summary = {
            "total_enquiries": db.query(Request)
            .filter(Request.classification == "General Enquiry")
            .count(),

            "resolved": db.query(Request)
            .filter(
                Request.classification == "General Enquiry",
                Request.status == "Resolved"
            )
            .count(),

            "average_confidence": db.query(
                func.avg(Request.confidence)
            )
            .filter(Request.classification == "General Enquiry")
            .scalar(),
        }

        recent = (
            db.query(Request)
            .filter(Request.classification == "General Enquiry")
            .order_by(Request.created_at.desc())
            .limit(20)
            .all()
        )

        return {
            "summary": summary,
            "recent_requests": [
                {
                    "id": r.id,
                    "request": r.request,
                    "classification": r.classification,
                    "urgency": r.urgency,
                    "status": r.status,
                    "assigned_team": r.assigned_team,
                    "created_at": r.created_at.isoformat() if r.created_at else None,
                    "highPriority": r.highPriority,
                }
                for r in recent
            ],
        }

    finally:
        db.close()
