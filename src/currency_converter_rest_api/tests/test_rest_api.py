from typing import Tuple
import pytest

from fastapi.testclient import TestClient

from ..app import app


@pytest.mark.parametrize(
    "currencies",
    [
        ("USD", "EUR"),
        ("EUR", "USD"),
        ("GBP", "EUR"),
        ("EUR", "GBP"),
        ("USD", "JPY"),
        ("JPY", "USD"),
        ("USD", "PLN"),
        ("PLN", "USD"),
    ],
)
def test_popular_currencies_exchange(currencies: Tuple):
    """Requires network connection to test.
    It only verifies if the connection was successful and output is OK.
    returns assertion error when required fields are missing or when quantity is invalid.
    """
    client = TestClient(app)
    ccy_from, ccy_to = currencies

    response = client.get(
        "/api/v1/currency/converter",
        params={"quantity": 1000, "ccy_from": ccy_from, "ccy_to": ccy_to},
    )
    d = response.json()

    assert "quantity" in d
    assert "ccy" in d
    assert d["quantity"] > 0, "exchanged quantity should be greater than 0."
