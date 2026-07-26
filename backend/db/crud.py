from db.database import SessionLocal
from db.models import Request

def save_request(**kwargs):
    db = SessionLocal()

    try:
        request = Request(**kwargs)

        db.add(request)
        db.commit()
        db.refresh(request)

        return request

    finally:
        db.close()