"""Duplication probe B: identical to duplication_probe_a on purpose."""

def summarize_orders(orders):
    """Aggregate a list of order dicts into a small report."""
    total = 0
    count = 0
    largest = None
    smallest = None
    by_status = {}
    by_customer = {}
    for order in orders:
        amount = order.get("amount", 0)
        status = order.get("status", "unknown")
        customer = order.get("customer", "anonymous")
        total = total + amount
        count = count + 1
        if largest is None or amount > largest:
            largest = amount
        if smallest is None or amount < smallest:
            smallest = amount
        by_status[status] = by_status.get(status, 0) + 1
        by_customer[customer] = by_customer.get(customer, 0) + amount
    average = total / count if count else 0
    top_customer = None
    top_amount = 0
    for customer, amount in by_customer.items():
        if amount > top_amount:
            top_customer = customer
            top_amount = amount
    report = {
        "total": total,
        "count": count,
        "average": average,
        "largest": largest,
        "smallest": smallest,
        "by_status": by_status,
        "top_customer": top_customer,
        "top_amount": top_amount,
    }
    return report


def format_report(report):
    """Render the report as lines of text."""
    lines = []
    lines.append("Total: " + str(report["total"]))
    lines.append("Count: " + str(report["count"]))
    lines.append("Average: " + str(report["average"]))
    lines.append("Largest: " + str(report["largest"]))
    lines.append("Smallest: " + str(report["smallest"]))
    for status, number in sorted(report["by_status"].items()):
        lines.append("Status " + status + ": " + str(number))
    lines.append("Top customer: " + str(report["top_customer"]))
    lines.append("Top amount: " + str(report["top_amount"]))
    return "\n".join(lines)
