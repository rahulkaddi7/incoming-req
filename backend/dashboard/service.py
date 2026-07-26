from sqlalchemy import func
from db.database import SessionLocal
from db.models import Request

def service_dashboard():
    db = SessionLocal()

    try:
        summary = {
            "total_requests": db.query(Request)
            .filter(Request.classification == "Service Request")
            .count(),
        }

        by_service = (
            db.query(
                Request.service_type,
                func.count(Request.id)
            )
            .filter(Request.classification == "Service Request")
            .group_by(Request.service_type)
            .all()
        )

        by_team = (
            db.query(
                Request.assigned_team,
                func.count(Request.id)
            )
            .filter(Request.classification == "Service Request")
            .group_by(Request.assigned_team)
            .all()
        )

        by_status = (
            db.query(
                Request.status,
                func.count(Request.id)
            )
            .filter(Request.classification == "Service Request")
            .group_by(Request.status)
            .all()
        )

        recent = (
            db.query(Request)
            .filter(Request.classification == "Service Request")
            .order_by(Request.created_at.desc())
            .limit(20)
            .all()
        )

        return {
            "summary": summary,
            "by_service": [
                {
                    "service_type": service,
                    "count": count
                }
                for service, count in by_service
            ],
            "by_team": [
                {
                    "team": team,
                    "count": count
                }
                for team, count in by_team
            ],
            "by_status": [
                {
                    "status": status,
                    "count": count
                }
                for status, count in by_status
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
