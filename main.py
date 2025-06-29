from fastapi import FastAPI
from app.controllers.chat_controller import router as chat_router
from app.controllers.history_controller import router as history_router
from infra.clients.mongo_client import MongoClient
from infra.exceptions.handlers import register_exception_handlers
from infra.logging.logging_config import configure_logging

configure_logging()

async def lifespan(app: FastAPI):
  MongoClient.connect()
  await MongoClient.create_indexes()
  yield

app = FastAPI(lifespan=lifespan)
register_exception_handlers(app)
app.include_router(chat_router)
app.include_router(history_router)
