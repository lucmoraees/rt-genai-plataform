from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from domain.exceptions.chat_exceptions import LLMGenerationException
from domain.exceptions.history_exceptions import HistoryNotFoundException, HistoryQueryException
import logging

logger = logging.getLogger("handlers")

def register_exception_handlers(app: FastAPI):

    def format_error_response(exc: Exception):
      return {
        "message": getattr(exc, "message", "Erro não identificado"),
        "error": getattr(exc, "original_error", None),
        "status_code": getattr(exc, "status_code", 500)
      }

    @app.exception_handler(LLMGenerationException)
    async def llm_generation_exception_handler(request: Request, exc: LLMGenerationException):
      logger.warning(f"[LLM ERROR] {exc.message} | {exc.original_error}")
      return JSONResponse(status_code=exc.status_code, content=format_error_response(exc))

    @app.exception_handler(HistoryNotFoundException)
    async def history_not_found_exception_handler(request: Request, exc: HistoryNotFoundException):
      logger.info(f"[HISTORY] {exc.message}")
      return JSONResponse(status_code=exc.status_code, content=format_error_response(exc))

    @app.exception_handler(HistoryQueryException)
    async def history_query_exception_handler(request: Request, exc: HistoryQueryException):
      logger.error(f"[HISTORY QUERY ERROR] {exc.message} | {exc.original_error}")
      return JSONResponse(status_code=exc.status_code, content=format_error_response(exc))

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
      logger.exception("[UNHANDLED ERROR]", exc_info=exc)
      return JSONResponse(status_code=500, content={
        "message": "Erro interno no servidor",
        "error": str(exc),
        "status_code": 500
      })
