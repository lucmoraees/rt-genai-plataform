class LLMGenerationException(Exception):
  def __init__(self, model: str, original_error: str):
    self.message = f"Erro ao gerar resposta com o modelo '{model}'"
    self.original_error = original_error
    self.status_code = 502
    super().__init__(self.message)
