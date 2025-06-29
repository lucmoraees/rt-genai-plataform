from domain.entities.history import HistoryItem
from domain.interfaces.history_repository_interface import HistoryRepositoryInterface

class SaveChatHistoryUseCase:
  def __init__(self, history_repository: HistoryRepositoryInterface):
    self.history_repository = history_repository

  async def execute(self, history: HistoryItem):
    await self.history_repository.save(history)