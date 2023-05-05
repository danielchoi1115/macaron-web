from fastapi import FastAPI, APIRouter
from app import api
from fastapi.staticfiles import StaticFiles
from app.core import get_settings, Settings
import logging


def get_application(settings: Settings = get_settings()) -> FastAPI:
    app = FastAPI(title="Ginger Macaron", openapi_url="/openapi.json")
    root_router = APIRouter()

    app.include_router(api.api_router, prefix=settings.API_V1_STR)
    app.include_router(api.template_router)
    app.include_router(root_router)
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    return app


app = get_application()


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("/home/sychoi/macaron-web/access.log")
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", reload=True)
