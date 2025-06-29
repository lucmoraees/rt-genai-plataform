import logging
from fastapi import APIRouter
from app.dto.chat_dto import ChatRequestDTO
from app.mapper.chat_mapper import ChatMapper
from dependency_injection import chat_service;

logger = logging.getLogger("chat-controller")

router = APIRouter()

@router.post("/v1/chat", tags=["Chat"], summary="Ask something to LLM")
async def chat_controller(payload: ChatRequestDTO):
  logger.info(f"Received chat request from user_id={payload.userId} using model={payload.model.value}")
  chat = await chat_service.handle_chat(payload)
  return ChatMapper.to_chat_response_dto(chat)
