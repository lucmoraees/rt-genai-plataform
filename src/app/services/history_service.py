import logging
from typing import List
from app.dto.history_dto import HistoryItemDTO, HistoryRequestQueryDTO
from app.mapper.history_mapper import HistoryMapper
from domain.useCases.get_history_use_case import GetHistoryUseCase

logger = logging.getLogger("history-service")

class HistoryService:
  def __init__(self, get_history_use_case: GetHistoryUseCase):
    self.get_history_use_case = get_history_use_case
    pass

  async def get_history(self, userId: str, params: HistoryRequestQueryDTO) -> List[HistoryItemDTO]:
    logger.info(f"Fetching history for user_id={userId} with model={params.model}, page={params.page}, limit={params.limit}")

    history = await self.get_history_use_case.execute(
      user_id=userId,
      model=params.model.value if params.model else None,
      page=params.page,
      limit=params.limit,
      order_by=params.orderBy,
      order=params.order
    )

    response = [
      HistoryMapper.to_dto(item) for item in history
    ]

    return response
