from fastapi import FastAPI
from app.controllers.chat_controller import router as chat_router
from app.controllers.history_controller import router as history_router
from infra.clients.mongo_client import MongoClient
from infra.exceptions.handlers import register_exception_handlers
from infra.logging.logging_config import configure_logging
from fastapi.middleware.cors import CORSMiddleware

async def lifespan(app: FastAPI):
  MongoClient.connect()
  await MongoClient.create_indexes()
  yield

app = FastAPI(lifespan=lifespan)

origins = [
  "http://localhost:8000",
  "http://127.0.0.1:8000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

configure_logging()
register_exception_handlers(app)

# Routes
app.include_router(chat_router)
app.include_router(history_router)
