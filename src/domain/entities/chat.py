from datetime import datetime
from uuid import uuid4

class Chat:
    def __init__(self, id: str, user_id: str, user_prompt: str, response: str, model: str, timestamp: datetime, system_prompt: str, temperature: float):
      self.id = id
      self.user_id = user_id
      self.user_prompt = user_prompt
      self.response = response
      self.model = model
      self.timestamp = timestamp
      self.system_prompt = system_prompt
      self.temperature = temperature

    @classmethod
    def create(cls, user_id: str, user_prompt: str, response: str, model: str, system_prompt: str, temperature: float):
      return cls(
        id=str(uuid4()),
        user_id=user_id,
        user_prompt=user_prompt,
        response=response,
        model=model,
        system_prompt=system_prompt,
        temperature=temperature,
        timestamp=datetime.now()
      )
