from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.features.auth.dependencies import get_current_user
from app.features.categories import service
from app.features.categories.schemas import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from app.features.users.models import User

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("", response_model=list[CategoryResponse])
def get_categories(
    db:Session = Depends(get_db),
    current_user: User=Depends(get_current_user)
):
    return service.get_all_categories(db, current_user.id)

@router.post("", response_model=CategoryResponse, status_code=201)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return service.create_category(db, current_user.id, data)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    data:CategoryUpdate,
    db:Session =Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    category = service.update_category(db, category_id, current_user.id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", status_code=204)
def delete_category(
    category_id: int,
    db:Session =Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    deleted = service.delete_category(db, category_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
