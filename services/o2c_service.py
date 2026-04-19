from services.validation import check_stock
from services.accounting import post_entry

def run_o2c_process(customer, material, qty):
    steps = []

    # Step 1: Sales Order
    steps.append("Step 1: Sales Order Created (VA01) → VBAK, VBAP")

    # Step 2: ATP Check
    if check_stock(material, qty):
        steps.append("Step 2: ATP Check Passed")

        # Step 3: Delivery
        steps.append("Step 3: Delivery Created (VL01N) → LIKP, LIPS")

        # Step 4: Goods Issue
        steps.append("Step 4: Goods Issue Posted (VL02N, Mvt 601)")
        steps.append(post_entry("COGS", "Inventory"))

        # Step 5: Billing
        steps.append("Step 5: Billing Generated (VF01)")
        steps.append(post_entry("Customer", "Revenue"))

        # Step 6: Payment
        steps.append("Step 6: Payment Received (F-28)")
        steps.append(post_entry("Bank", "Customer"))

    else:
        steps.append("ATP Check Failed → Insufficient Stock")

    return steps