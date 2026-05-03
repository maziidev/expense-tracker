from decimal import Decimal
from pydantic import BaseModel


class CategorySummary(BaseModel):
    category_id: int | None
    category_name: str | None
    total: Decimal
    count: int

    model_config = {"from_attributes": True}


class MonthlySummary(BaseModel):
    month: str
    total: Decimal
    count: int


class AnalyticsSummary(BaseModel):
    total_this_month: Decimal
    total_last_month: Decimal
    total_all_time: Decimal
    expense_count_this_month: int
    highest_category: str | None