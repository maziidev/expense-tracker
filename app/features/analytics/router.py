from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.features.auth.dependencies import get_current_user
from app.features.analytics import service
from app.features.analytics.schemas import (
    AnalyticsSummary,
    CategorySummary,
)
from app.features.users.models import User

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary", response_model=AnalyticsSummary)
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.get_summary(db, current_user.id)


@router.get("/by-category", response_model=list[CategorySummary])
def get_by_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.get_by_category(db, current_user.id)


@router.get("/daily")
def get_daily(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.get_daily_breakdown(db, current_user.id)