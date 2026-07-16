from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database import get_db

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live", status_code=status.HTTP_200_OK)
def liveness() -> dict[str, str]:
    """Process is up. No dependency checks — used for restart decisions."""
    return {"status": "ok"}


@router.get("/ready", status_code=status.HTTP_200_OK)
def readiness(db: Session = Depends(get_db)) -> dict[str, str]:
    """Process can serve traffic — verifies the DB is reachable."""
    db.execute(text("SELECT 1"))
    return {"status": "ok"}