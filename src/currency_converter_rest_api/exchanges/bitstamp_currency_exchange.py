import logging

import httpx
from .currency_exchange_base import CurrencyExchangeBase

_logger = logging.getLogger(__name__)


class BitstampCurrencyExchange(CurrencyExchangeBase):

    async def get_price(self, currency: str) -> float:
        api_url: str = "https://www.bitstamp.net/api/v2/ticker/BTC{symbol}"
        api_url = api_url.format(symbol=currency.upper())
        async with httpx.AsyncClient() as client:
            _logger.info(f"Calling GET {api_url}")
            response = await client.get(api_url)
            d = response.json()
            return float(d.get("last", -1))
