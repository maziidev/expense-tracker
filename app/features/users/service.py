from sqlalchemy.orm import Session

from app.features.auth.service import hash_password
from app.features.users.models import User
from app.features.users.schemas import UserCreate, UserUpdate


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id==user_id).first()

def get_user_by_email(db:Session, email: str) -> User | None:
    return db.query(User).filter(User.email==email).first()

def create_user(db:Session, data: UserCreate) -> User | None:
    existing = get_user_by_email(db, data.email)
    if existing:
        return None

    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user_id: int, data: UserUpdate) -> User | None:
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    user.username = data.username
    user.email = data.email
    if data.password:
        user.password = hash_password(data.password)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    user = get_user_by_id(db, user_id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
