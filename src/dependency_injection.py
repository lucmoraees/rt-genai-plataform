from app.services.history_service import HistoryService
from domain.useCases.get_history_use_case import GetHistoryUseCase
from infra.providers.gemini_provider import GeminiProvider
from domain.useCases.create_chat_use_case import CreateChatUseCase
from app.services.chat_service import ChatService
from domain.useCases.save_chat_history_use_case import SaveChatHistoryUseCase
from dotenv import load_dotenv

from infra.repositories.history_repository import HistoryRepository

load_dotenv()

# Providers
gemini = GeminiProvider()

# Repositories
history_repository = HistoryRepository()

# Use Cases
chat_use_case = CreateChatUseCase(llm_provider=gemini)
save_chat_history_use_case = SaveChatHistoryUseCase(history_repository=history_repository)
get_history_use_case = GetHistoryUseCase(history_repository=history_repository)

# Services
chat_service = ChatService(chat_use_case=chat_use_case, save_chat_history_use_case=save_chat_history_use_case)
history_service = HistoryService(get_history_use_case=get_history_use_case)
