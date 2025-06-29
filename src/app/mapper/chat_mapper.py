from domain.entities.chat import Chat
from app.dto.chat_dto import ChatResponseDTO


class ChatMapper:
  @staticmethod
  def to_chat_response_dto(chat: Chat) -> ChatResponseDTO:
    return ChatResponseDTO(
      id=chat.id,
      userId=chat.user_id,
      userPrompt=chat.user_prompt,
      response=chat.response,
      model=chat.model,
      systemPrompt=chat.system_prompt,
      temperature=chat.temperature,
      timestamp=chat.timestamp
    )