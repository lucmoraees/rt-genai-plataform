from datetime import datetime
from uuid import uuid4

class HistoryItem:
  def __init__(self, id: str, user_id: str, user_prompt: str, response: str, model: str, timestamp: datetime, system_prompt: str, temperature: float, llm_response_seconds: float):
    self.id = id
    self.user_id = user_id
    self.user_prompt = user_prompt
    self.response = response
    self.model = model
    self.timestamp = timestamp
    self.system_prompt = system_prompt
    self.temperature = temperature
    self.llm_response_seconds = llm_response_seconds

  @classmethod
  def create(cls, user_id: str, user_prompt: str, response: str, model: str, system_prompt: str, temperature: float, llm_response_seconds: float):
    return cls(
      id=str(uuid4()),
      user_id=user_id,
      user_prompt=user_prompt,
      response=response,
      model=model,
      system_prompt=system_prompt,
      temperature=temperature,
      llm_response_seconds=llm_response_seconds,
      timestamp=datetime.now()
    )

  @classmethod
  def from_dict(cls, data: dict):
    return cls(
      id=str(data.get("_id")),
      user_id=data["userId"],
      user_prompt=data["userPrompt"],
      response=data["response"],
      model=data["model"],
      system_prompt=data["systemPrompt"],
      temperature=data["temperature"],
      timestamp=data["timestamp"],
      llm_response_seconds=data["llmResponseSeconds"]
    )

  def to_dict(self):
    return {
      "_id": self.id,
      "userId": self.user_id,
      "userPrompt": self.user_prompt,
      "model": self.model,
      "response": self.response,
      "systemPrompt": self.system_prompt,
      "temperature": self.temperature,
      "timestamp": self.timestamp,
      "llmResponseSeconds": self.llm_response_seconds
    }
