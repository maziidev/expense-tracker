from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.features.analytics.router import router as analytics_router
from app.features.auth.router import router as auth_router
from app.features.categories.models import Category  #noqa: F401
from app.features.categories.router import router as categories_router
from app.features.expenses.models import Expense  #noqa: F401
from app.features.expenses.router import router as expense_router
from app.features.users.models import User  #noqa: F401
from app.features.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.validate()
    yield

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)


app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(categories_router, prefix="/api/v1")
app.include_router(expense_router, prefix="/api/v1")
app.include_router(analytics_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    """
    Health check endpoint. usually called by loadbalancers and monitoring tools to verify the app is running.
    """
    return {
        "status": "Healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
    }