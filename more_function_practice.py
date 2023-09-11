def calculate_tax_for_the_shire(grossPay):
    # The friendly Shire has a 20% tax rate
    return grossPay * 0.2


def calculate_tax_for_mirkwood(grossPay):
    # Dodgy Mirkwood has a 50% tax rate
    return grossPay * 0.5


def calculate_tax_for_mordor(grossPay):
    # Terrible Mordor has a 90% tax rate plus a fixed tax of £50.
    return grossPay * 0.9 + 50

def standing_charge_for_shire(grossPay):
    return grossPay * 0.01

def standing_charge_for_mirkwood(grossPay):
    return grossPay * 0.02

def standing_charge_for_mordor(grossPay):
    return grossPay * 0.05

def report_pay(gross_pay, calculate_tax, standing_charge):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay) + standing_charge(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} which includes a standing charge of {standing_charge(gross_pay)}, making your net pay {net_pay}"


print("Frodo's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire, standing_charge_for_shire))
# Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

print("Bombadil's Pay:")
print(report_pay(5000.0, calculate_tax_for_mirkwood, standing_charge_for_mirkwood))
# Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

print("Mount Doom's Pay:")
print(report_pay(5000.0, calculate_tax_for_mordor, standing_charge_for_mordor))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0


# This is useful because it allows us to reuse the logic in report_pay with different tax formulas without having to change report_pay at all, or do any logic outside of the functions.

# Consider putting the above in a Python file, running it, and playing around with it. Try creating a new tax calculation function for a zero-tax, or a fixed tax rate, and pass it in to report_pay.