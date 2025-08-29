from abc import ABC, abstractmethod


class CurrencyExchangeBase(ABC):
    @abstractmethod
    async def get_price(self, currency: str) -> float:
        pass
