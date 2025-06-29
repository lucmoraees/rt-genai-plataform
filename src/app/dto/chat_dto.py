from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from domain.enums.gemini_models_enum import GeminiModels


class ChatRequestDTO(BaseModel):
  userId: str = Field(..., description="Identificador do usuário")
  userPrompt: str = Field(..., description="Mensagem enviada pelo usuário")
  model: GeminiModels = Field(..., description="Modelo Gemini a ser utilizado")
  temperature: Optional[float] = Field(
    default=0.7,
    ge=0.0,
    le=1.0,
    multiple_of=0.1,
    description="Temperatura entre 0.0 e 1.0, com uma casa decimal"
  )
  systemPrompt: Optional[str] = Field("", description="Prompt do sistema (opcional)")

class ChatResponseDTO(BaseModel):
  id: str
  userId: str
  userPrompt: str
  response: str
  model: str
  systemPrompt: str
  temperature: float
  timestamp: datetime
