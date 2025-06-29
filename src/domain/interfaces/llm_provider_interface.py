from abc import ABC, abstractmethod

class LLMProviderInterface(ABC):
  @abstractmethod
  def generate_text(self, user_prompt: str, model: str, system_prompt: str, temperature: float) -> str:
    pass
