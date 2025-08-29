import logging
from typing import Annotated
from fastapi import APIRouter, Depends, Response
from ..services.currency_exchange_service import CurrencyExchangeService

_logger = logging.getLogger(__name__)

router = APIRouter(prefix="/currency", tags=["currency"])

ExchangeServiceDep = Annotated[
    CurrencyExchangeService, Depends(CurrencyExchangeService)
]


@router.get("/converter")
async def currency_converter(
    exchange_service: ExchangeServiceDep,
    ccy_from: str,
    ccy_to: str,
    quantity: float,
    response: Response,
):
    """Converts currencies using exchange service."""
    _logger.info(
        f"User requested currency convertion: {ccy_from=} {ccy_to=} {quantity=} "
    )
    try:
        assert quantity > 0, "quantity should be greater than 0."
        ratio = await exchange_service.get_exchange_rate(ccy_from, ccy_to)
        return {"quantity": round(quantity / ratio, 2), "ccy": ccy_to}
    except Exception as e:
        response.status_code = 400
        return {"error": str(e)}
