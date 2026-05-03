from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.features.auth.dependencies import get_current_user
from app.features.users import service
from app.features.users.models import User
from app.features.users.schemas import UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserResponse)
def update_me(data: UserUpdate, db:Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    updated = service.update_user(db, current_user.id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="user not found")
    return updated

@router.delete("/me", status_code=204)
def delete_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service.delete_user(db, current_user.id)