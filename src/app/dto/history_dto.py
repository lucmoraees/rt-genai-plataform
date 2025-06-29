from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from domain.enums.gemini_models_enum import GeminiModels
from domain.enums.order_enum import Order

class HistoryItemDTO(BaseModel):
  id: str
  userId: str
  userPrompt: str
  response: str
  model: str
  systemPrompt: str
  temperature: float
  timestamp: datetime
  llmResponseTimeS: Optional[float]

class HistoryResponseDTO(BaseModel):
  history: List[HistoryItemDTO]

class HistoryRequestQueryDTO(BaseModel):
  model: Optional[GeminiModels] = Field(None, description="Modelo de LLM usado")
  page: int = Field(1, gt=0, description="Número da página")
  limit: int = Field(10, gt=0, description="Número de itens por página")
  orderBy: str = Field("timestamp", description="Campo para ordenação")
  order: Order = Field(Order.DESC.value, description="Direção da ordenação (asc ou desc)")