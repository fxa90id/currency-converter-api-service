from fastapi import FastAPI, APIRouter

from .config import APP_NAME, APP_VERSION, DEBUG
from .routes.currency import router as currency_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(currency_router)

app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=DEBUG)

app.include_router(api_router)
