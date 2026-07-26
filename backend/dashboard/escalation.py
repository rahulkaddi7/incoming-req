from sqlalchemy import func
from db.database import SessionLocal
from db.models import Request

def escalation_dashboard():
    db = SessionLocal()

    try:
        summary = {
            "total_escalations": db.query(Request)
            .filter(Request.classification == "Escalation")
            .count(),

            "critical_cases": db.query(Request)
            .filter(Request.highPriority == True)
            .count(),

            "pending_review": db.query(Request)
            .filter(
                Request.classification == "Escalation",
                Request.status == "Escalated"
            )
            .count(),
        }

        by_team = (
            db.query(
                Request.assigned_team,
                func.count(Request.id)
            )
            .filter(Request.classification == "Escalation")
            .group_by(Request.assigned_team)
            .all()
        )

        recent = (
            db.query(Request)
            .filter(Request.classification == "Escalation")
            .order_by(Request.created_at.desc())
            .limit(20)
            .all()
        )

        return {
            "summary": summary,

            "by_team": [
                {
                    "team": team,
                    "count": count
                }
                for team, count in by_team
            ],

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