import logging

import httpx
from .currency_exchange_base import CurrencyExchangeBase

_logger = logging.getLogger(__name__)


def _convert_to_tether(currency: str) -> str:
    """Convert Currency to Tether"""
    match currency.upper():
        case "USD":
            return "USDT"
        case _:
            return currency


class BinanceCurrencyExchange(CurrencyExchangeBase):

    async def get_price(self, currency: str) -> float:
        api_url: str = "https://api3.binance.com/api/v3/ticker/price?symbol=BTC{symbol}"
        api_url = api_url.format(symbol=_convert_to_tether(currency))
        async with httpx.AsyncClient() as client:
            _logger.info(f"Calling GET {api_url}")
            response = await client.get(api_url)
            d = response.json()
            if response.status_code == 200:
                assert "price" in d
                return float(d["price"])
            else:
                raise Exception(d["msg"])
