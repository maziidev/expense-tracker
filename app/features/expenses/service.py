from sqlalchemy.orm import Session

from app.features.expenses.models import Expense
from app.features.expenses.schemas import ExpenseCreate, ExpenseUpdate


def get_all_expenses(db:Session, user_id:int) -> list[Expense]:
    return db.query(Expense).filter(Expense.user_id==user_id).all()

def get_expenses_by_id(db:Session, expenses_id: int, user_id:int)-> Expense | None:
    return db.query(Expense).filter(Expense.id == expenses_id, Expense.user_id==user_id).first()

def create_expense(db:Session, user_id: int, data: ExpenseCreate) -> Expense:
    expense = Expense(
        title = data.title,
        amount=data.amount,
        date=data.date,
        note=data.note,
        category_id=data.category_id,
        user_id=user_id
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def update_expense(db:Session, expenses_id: int, user_id:int, data:ExpenseUpdate) -> Expense | None:
    exp = get_expenses_by_id(db, expenses_id, user_id)
    if not exp:
        return None

    exp.title = data.title
    exp.note=data.note
    exp.amount=data.amount
    exp.date=data.date
    db.commit()
    db.refresh(exp)
    return exp

def delete_expense(db:Session, expenses_id: int, user_id: int) -> bool:
    exp = get_expenses_by_id(db, expenses_id, user_id)
    if not exp:
        return False
    db.delete(exp)
    db.commit()
    return True