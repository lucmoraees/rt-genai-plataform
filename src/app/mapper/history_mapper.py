from app.dto.history_dto import HistoryItemDTO
from domain.entities.history import HistoryItem


class HistoryMapper:
  @staticmethod
  def to_dto(item: HistoryItem):
    return HistoryItemDTO(
      id=item.id,
      model=item.model,
      userPrompt=item.user_prompt,
      response=item.response,
      userId=item.user_id,
      timestamp=item.timestamp,
      systemPrompt=item.system_prompt,
      temperature=item.temperature,
      llmResponseSeconds=item.llm_response_seconds
    )
  
  @staticmethod
  def to_entity(item: HistoryItemDTO):
    return HistoryItem(
      id=item.id,
      model=item.model,
      user_prompt=item.userPrompt,
      response=item.response,
      user_id=item.userId,
      timestamp=item.timestamp,
      system_prompt=item.systemPrompt,
      temperature=item.temperature,
      llm_response_seconds=item.llmResponseSeconds
    )