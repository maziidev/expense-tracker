from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description =Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Foreign Key - this column stores the user's id
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False )

    # relationships
    user = relationship("User", back_populates="categories")
    expenses = relationship("Expense", back_populates="category")