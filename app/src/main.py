from fastapi import FastAPI
from starlette.requests import Request

from utils import settings
from db.session import Session, init_db
from routes import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION
    )
    application.include_router(
        api_router,
    )
    return application


app = get_application()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get('/_healthz', status_code=200)
def healthcheckk():
    return {'healthcheck': 'true'}
