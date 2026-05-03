from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    amount: Decimal = Field(..., gt=0, decimal_places=2)
    date: date
    note: str | None = Field(None)
    category_id: int | None = None

class ExpenseUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    amount: Decimal=Field(..., gt=0, decimal_places=2)
    date: date
    note: str | None = Field(None)
    category_id: int | None = None


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: Decimal
    date: date
    note: str | None
    category_id: int | None
    created_at: datetime

    model_config = {"from_attributes": True}

class ExpenseFilters(BaseModel):
    """Query Parameters for filtering expenses"""
    category_id: int | None = None
    start_date: date | None = None
    end_date: date | None = None
    min_amount: Decimal | None = None
    max_amount: Decimal | None = None