from sqlalchemy.orm import Session

from app.features.categories.models import Category
from app.features.categories.schemas import CategoryCreate, CategoryUpdate


def get_all_categories(db:Session, user_id: int) -> list[Category]:
    return db.query(Category).filter(Category.user_id == user_id).all()

def get_category_by_id(db:Session, category_id: int, user_id:int)-> Category | None:
    return db.query(Category).filter(Category.id == category_id, Category.user_id==user_id).first()

def create_category(db:Session, user_id: int, data: CategoryCreate) -> Category:
    cat = Category(
        name = data.name,
        description=data.description,
        user_id=user_id
    )
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def update_category(db:Session, category_id: int, user_id:int, data:CategoryUpdate) -> Category | None:
    cate = get_category_by_id(db, category_id, user_id)
    if not cate:
        return None

    cate.name = data.name
    cate.description=data.description
    db.commit()
    db.refresh(cate)
    return cate

def delete_category(db:Session, category_id: int, user_id: int) -> bool:
    catee = get_category_by_id(db, category_id, user_id)
    if not catee:
        return False
    db.delete(catee)
    db.commit()
    return True