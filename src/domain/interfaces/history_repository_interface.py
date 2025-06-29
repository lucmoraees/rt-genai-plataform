from abc import ABC, abstractmethod
from typing import List
from domain.entities.history import HistoryItem

class HistoryRepositoryInterface(ABC):

  @abstractmethod
  async def save(self, history: HistoryItem) -> None:
    pass

  @abstractmethod
  async def find_by_filters() -> List[HistoryItem]:
    pass
