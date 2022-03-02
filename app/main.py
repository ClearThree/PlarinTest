from logging import getLogger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import config
from app.api_routers.v1.router import v1router
from app.db.connector import mongo_connector
from app.schemas.base_validation import GetPingResponse
from app.utils.logger import set_logging_parameters


LOGGER = set_logging_parameters(getLogger(__name__))

app = FastAPI(title=config.APP_TITLE, description=config.APP_DESCRIPTION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=config.ALLOWED_CREDENTIALS,
    allow_methods=config.ALLOWED_METHODS,
    allow_headers=config.ALLOWED_HEADERS,
)

app.include_router(v1router, prefix="/api")  # include the router for first version of API.


@app.on_event("startup")
async def startup_event():
    LOGGER.info("The application is starting...")
    LOGGER.info("Connecting to Mongo DB ... in progress.")
    try:
        await mongo_connector.connect()
    except ConnectionError:
        LOGGER.warning("Connecting to Mongo DB ... Error!")
        LOGGER.exception("Error during Mongo connection: ")
    else:
        LOGGER.info("Connecting to Mongo DB ... Done.")
        LOGGER.info("The application started successfully.")


@app.on_event("shutdown")
async def shutdown_event():
    LOGGER.info("The application is shutting down...")
    LOGGER.info("Disconnecting Mongo DB ... in progress.")
    try:
        await mongo_connector.connect()
    except ConnectionError:
        LOGGER.warning("Disconnecting Mongo DB ... Error!")
        LOGGER.exception("Error during Mongo disconnection: ")
    else:
        LOGGER.info("Disconnecting Mongo DB ... Done.")
        LOGGER.info("The application shut down successfully.")


@app.get("/ping", status_code=200, response_model=GetPingResponse)
async def pong():
    return "pong"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
