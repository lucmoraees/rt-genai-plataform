from pymongo import ASCENDING, DESCENDING
from typing import List, Optional
from domain.entities.history import HistoryItem
from infra.clients.mongo_client import MongoClient

from domain.interfaces.history_repository_interface import HistoryRepositoryInterface

class HistoryRepository(HistoryRepositoryInterface):
    def client(self):
      return MongoClient.get_db()["history"]

    async def save(self, history: HistoryItem) -> None:
      await self.client().insert_one(history.to_dict())

    async def find_by_filters(
      self,
      user_id: str,
      model: Optional[str] = None,
      page: int = 1,
      limit: int = 10,
      order_by: str = "timestamp",
      order: str = "desc"
    ) -> List[HistoryItem]:
      query = {"userId": user_id}

      if model:
        query["model"] = model

      skip = (page - 1) * limit
      sort_direction = DESCENDING if order == "desc" else ASCENDING

      cursor = self.client().find(query).sort(order_by, sort_direction).skip(skip).limit(limit)

      results = []
      async for document in cursor:
        results.append(HistoryItem.from_dict(document))

      return results
