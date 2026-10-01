"""Uses the shared models package, like an API project importing its models project."""

from dd_sandbox_models import Subscriber, normalize_msisdn

from sandbox.pricing import apply_discount

PLAN_PRICES = {"basic": 10.0, "plus": 25.0}


def quote(raw_msisdn: str, plan: str, percent: float = 0) -> tuple[Subscriber, float]:
    subscriber = Subscriber(msisdn=normalize_msisdn(raw_msisdn), plan=plan)
    return subscriber, apply_discount(PLAN_PRICES[plan], percent)
