import logging
from fastapi import APIRouter, Depends
from app.dto.history_dto import HistoryRequestQueryDTO, HistoryResponseDTO
from dependency_injection import history_service;

logger = logging.getLogger("history-controller")

router = APIRouter()

@router.get("/v1/history/{userId}", tags=["History"], summary="Consult interactions with llm history")
async def history_controller(userId: str, params: HistoryRequestQueryDTO = Depends()) -> HistoryResponseDTO:
  logger.info(f"Received history request from userId={userId}")
  history = await history_service.get_history(userId, params)
  return HistoryResponseDTO(history=history)
