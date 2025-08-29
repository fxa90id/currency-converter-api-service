from fastapi import FastAPI, APIRouter

from .config import APP_NAME, APP_VERSION, DEBUG

api_router = APIRouter(prefix="/api/v1")

app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=DEBUG)

app.include_router(api_router)
