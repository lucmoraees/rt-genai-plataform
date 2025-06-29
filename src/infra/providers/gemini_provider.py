from google import genai
from google.genai import types
from domain.exceptions.chat_exceptions import LLMGenerationException
from domain.interfaces.llm_provider_interface import LLMProviderInterface

class GeminiProvider(LLMProviderInterface):
  def __init__(self):
    self.client = genai.Client()

  def generate_text(self, user_prompt: str, model: str, system_prompt: str = "", temperature: float = 0.7) -> str:
    try:
      response = self.client.models.generate_content(
        model=model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
          system_instruction=system_prompt,
          temperature=temperature
        )
      )

      return response.text
    except Exception as e:
      raise LLMGenerationException(model=model, original_error=str(e))
