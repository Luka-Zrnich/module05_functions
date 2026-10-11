# business_rules.py
# Author: Luka Zrnich

APPROVAL_LIMIT = 1000  # module level constant


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return true if amount exceeds approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Returns the approval tier based on the amount."""
    if amount <= 500:
        return "Auto"
    elif amount <= 2000:
        return "Manager"
    else:
        return "Director"


def apply_discount(price: float, pct: float) -> float:
    """Return price after discount. pct is 0-100"""
    return price * (1 - pct / 100)
