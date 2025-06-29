from typing import List
from domain.entities.history import HistoryItem
from domain.interfaces.history_repository_interface import HistoryRepositoryInterface
from domain.exceptions.history_exceptions import HistoryNotFoundException, HistoryQueryException

class GetHistoryUseCase:
  def __init__(self, history_repository: HistoryRepositoryInterface):
    self.history_repository = history_repository
    pass

  async def execute(self, user_id: str, model=None, page=1, limit=10, order_by="timestamp", order="desc") -> List[HistoryItem]:
    try:
        results = await self.history_repository.find_by_filters(
           user_id,model, page, limit, order_by, order)

        if not results:
          raise HistoryNotFoundException(user_id)

        return results
    except HistoryNotFoundException:
        raise
    except Exception as e:
        raise HistoryQueryException(str(e))
