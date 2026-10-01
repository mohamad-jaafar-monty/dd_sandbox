import pytest

from sandbox.service import quote


def test_quote_normalizes_and_prices():
    subscriber, price = quote("+961 70 123 456", "plus", 20)
    assert subscriber.msisdn == "+96170123456"
    assert price == 20.0


def test_quote_rejects_short_numbers():
    with pytest.raises(ValueError):
        quote("123", "basic")
