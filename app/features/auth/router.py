from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.features.auth.schemas import LoginRequest, TokenResponse
from app.features.auth.service import create_access_token, verify_password
from app.features.users.models import User
from app.features.users.schemas import UserCreate, UserResponse
from app.features.users.service import create_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserCreate, db: Session=Depends(get_db)):
    user = create_user(db, data)
    if not user:
        raise HTTPException(status_code=409, detail="Email already registered")
    return user

@router.post("/login", response_model=TokenResponse)
def login(data:LoginRequest, db: Session=Depends(get_db)):
    user=db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid credentials",
        )

    token = create_access_token(user.id)
    return TokenResponse(access_token=token)