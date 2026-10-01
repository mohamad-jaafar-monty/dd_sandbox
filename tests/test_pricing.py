import pytest

from sandbox.pricing import apply_discount, bundle_total


def test_apply_discount_rounds_to_cents():
    assert apply_discount(10, 15) == 8.5
    assert apply_discount(9.99, 33) == 6.69


def test_apply_discount_rejects_out_of_range():
    with pytest.raises(ValueError):
        apply_discount(10, 150)


def test_bundle_total_sums_then_discounts():
    assert bundle_total([10, 20, 30], 10) == 54.0
