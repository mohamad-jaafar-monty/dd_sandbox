"""Pure pricing helpers; no dependencies, so the baseline coverage run has something to measure."""


def apply_discount(amount: float, percent: float) -> float:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)


def bundle_total(prices: list[float], percent: float = 0) -> float:
    return apply_discount(sum(prices), percent)
