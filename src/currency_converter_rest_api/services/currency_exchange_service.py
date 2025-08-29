from cachetools import TTLCache
from cachetools_async import cached

from ..config import DEFAULT_CACHE_TTL

from ..exchanges.bitstamp_currency_exchange import BitstampCurrencyExchange
from ..exchanges.binance_currency_exchange import BinanceCurrencyExchange


class CurrencyExchangeService:

    async def get_exchange_rate(self, ccy_from: str, ccy_to: str):
        from_price = await self._get_price(ccy_from)
        to_price = await self._get_price(ccy_to)
        return from_price / to_price

    @cached(
        cache=TTLCache(maxsize=512, ttl=DEFAULT_CACHE_TTL), key=lambda self, ccy: ccy
    )
    async def _get_price(self, ccy: str) -> float:
        match ccy:
            case "GBP":
                exchange = BitstampCurrencyExchange()
            case _:
                exchange = BinanceCurrencyExchange()
        return await exchange.get_price(ccy)
