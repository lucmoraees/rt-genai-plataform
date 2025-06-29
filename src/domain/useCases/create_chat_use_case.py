from domain.entities.chat import Chat
from domain.interfaces.llm_provider_interface import LLMProviderInterface

class CreateChatUseCase:
  def __init__(self, llm_provider: LLMProviderInterface):
    self.llm_provider = llm_provider

  def execute(self, user_id: str, user_prompt: str, model: str, system_prompt: str, temperature: float) -> Chat:
    response = self.llm_provider.generate_text(user_prompt, model, system_prompt, temperature)
    
    chat = Chat.create(response=response,
                       user_id=user_id,
                       user_prompt=user_prompt,
                       model=model,
                       system_prompt=system_prompt,
                       temperature=temperature)
    return chat
