import time
import logging
import asyncio
from app.dto.chat_dto import ChatRequestDTO
from domain.entities.chat import Chat
from domain.entities.history import HistoryItem
from domain.useCases.save_chat_history_use_case import SaveChatHistoryUseCase
from domain.useCases.create_chat_use_case import CreateChatUseCase

logger = logging.getLogger("chat-service")

class ChatService:
  def __init__(self, chat_use_case: CreateChatUseCase, save_chat_history_use_case: SaveChatHistoryUseCase):
    self.chat_use_case = chat_use_case
    self.save_chat_history_use_case = save_chat_history_use_case

  async def handle_chat(self, payload: ChatRequestDTO) -> Chat:
    start_time = time.monotonic()
    chat = self.chat_use_case.execute(payload.userId,
                                      payload.userPrompt,
                                      payload.model.value,
                                      payload.systemPrompt,
                                      payload.temperature)
    end_time = time.monotonic()
    duration = end_time - start_time
    logger.info(f"LLM response received in {duration:.2f}s for model={payload.model.value}")

    history = HistoryItem.create(model=chat.model,
                                 system_prompt=chat.system_prompt,
                                 temperature=chat.temperature,
                                 response=chat.response,
                                 user_id=chat.user_id,
                                 user_prompt=chat.user_prompt,
                                 llm_response_time_s=round(duration, 2))
    
    asyncio.create_task(self.save_chat_history_safe(history))

    return chat
  
  async def save_chat_history_safe(self, history: HistoryItem):
    try:
      logger.info(f"Saving chat history for user_id={history.user_id} at {history.timestamp}")
      await self.save_chat_history_use_case.execute(history)
      logger.info(f"Chat history saved for user_id={history.user_id}")
    except Exception as e:
      logger.error(f"Failed to save history: {e}")