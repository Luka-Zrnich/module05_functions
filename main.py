from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)

# add sample inputs
price, qty = 450.00, 3
total = calculate_total(price, qty)


print(f"Total: ${total:.2f}")
print(f"Requires review: {requires_review(total)}")
print(f"Approval tier: {get_approval_tier(total)}")
print(f"Price after 10% discount: ${apply_discount(total, 10):.2f}")
