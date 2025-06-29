class HistoryNotFoundException(Exception):
  def __init__(self, user_id: str):
    self.message = f"Histórico não encontrado para o user_id={user_id}"
    self.original_error = None
    self.status_code = 404
    super().__init__(self.message)


class HistoryQueryException(Exception):
  def __init__(self, original_error: str):
    self.message = "Erro ao consultar o histórico"
    self.original_error = original_error
    self.status_code = 500
    super().__init__(self.message)
