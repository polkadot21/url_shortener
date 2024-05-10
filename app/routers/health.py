from sqlalchemy import text

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.db.urls import get_db

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "details": str(e)}