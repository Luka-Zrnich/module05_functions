from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)


def test_requires_review_over():
    assert requires_review(1500) is True


def test_requires_review_under():
    assert requires_review(500) is False


def test_boundary_at_limit():
    # Exactly at 1000 should NOT require review (> not >=)
    assert requires_review(1000) is False


def test_total_includes_tacx():
    assert round(calculate_total(100, 2), 2) == 214.0


def test_tier_auto():
    assert get_approval_tier(400) == "Auto"


def test_tier_boundary():
    assert get_approval_tier(500) == "Auto"
    assert get_approval_tier(501) == "Manager"
    assert get_approval_tier(2000) == "Manager"
    assert get_approval_tier(2001) == "Director"


def test_tier_manager():
    assert get_approval_tier(1500) == "Manager"


def test_discount_ten():
    assert round(apply_discount(100.00, 10), 2) == 90.0
