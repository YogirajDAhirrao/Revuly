from fastapi import FastAPI
from pydantic_settings import BaseSettings

from app.db.init_db import init_db
from app.api.v1.review_routes import router as review_router
def create_app() -> FastAPI:
    app = FastAPI()

    @app.on_event("startup")
    def on_startup():
        init_db()

    @app.get("/health")
    def init():
        return {"status":"running"}
    
    app.include_router(review_router,prefix="/api/v1/review",tags=["Reviews"])

    return app    

app = create_app()

