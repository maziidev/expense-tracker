from datetime import date
from decimal import Decimal
from sqlalchemy import func, extract
from sqlalchemy.orm import Session
from app.features.expenses.models import Expense
from app.features.categories.models import Category


def get_summary(db: Session, user_id: int) -> dict:
    """Total spent this month, last month, and all time"""
    today = date.today()

    def month_total(month: int, year: int) -> Decimal:
        result = db.query(func.sum(Expense.amount)).filter(
            Expense.user_id == user_id,
            extract("month", Expense.date) == month,
            extract("year", Expense.date) == year,
        ).scalar()
        return result or Decimal("0.00")

    def month_count(month: int, year: int) -> int:
        return db.query(Expense).filter(
            Expense.user_id == user_id,
            extract("month", Expense.date) == month,
            extract("year", Expense.date) == year,
        ).count()

    # Calculate last month
    if today.month == 1:
        last_month = 12
        last_month_year = today.year - 1
    else:
        last_month = today.month - 1
        last_month_year = today.year

    # All time total
    all_time = db.query(func.sum(Expense.amount)).filter(
        Expense.user_id == user_id
    ).scalar() or Decimal("0.00")

    # Highest spending category this month
    top_category = db.query(
        Category.name,
        func.sum(Expense.amount).label("total")
    ).join(Expense, Expense.category_id == Category.id).filter(
        Expense.user_id == user_id,
        extract("month", Expense.date) == today.month,
        extract("year", Expense.date) == today.year,
    ).group_by(Category.name).order_by(
        func.sum(Expense.amount).desc()
    ).first()

    return {
        "total_this_month": month_total(today.month, today.year),
        "total_last_month": month_total(last_month, last_month_year),
        "total_all_time": all_time,
        "expense_count_this_month": month_count(today.month, today.year),
        "highest_category": top_category[0] if top_category else None,
    }


def get_by_category(db: Session, user_id: int) -> list:
    """Total spending per category"""
    results = db.query(
        Category.id,
        Category.name,
        func.sum(Expense.amount).label("total"),
        func.count(Expense.id).label("count"),
    ).join(Expense, Expense.category_id == Category.id).filter(
        Expense.user_id == user_id
    ).group_by(Category.id, Category.name).all()

    return [
        {
            "category_id": r.id,
            "category_name": r.name,
            "total": r.total,
            "count": r.count,
        }
        for r in results
    ]


def get_daily_breakdown(db: Session, user_id: int) -> list:
    """Daily spending for current month"""
    today = date.today()

    results = db.query(
        Expense.date,
        func.sum(Expense.amount).label("total"),
        func.count(Expense.id).label("count"),
    ).filter(
        Expense.user_id == user_id,
        extract("month", Expense.date) == today.month,
        extract("year", Expense.date) == today.year,
    ).group_by(Expense.date).order_by(Expense.date).all()

    return [
        {
            "date": str(r.date),
            "total": r.total,
            "count": r.count,
        }
        for r in results
    ]