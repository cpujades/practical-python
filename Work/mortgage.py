# mortgage.py
#
# Exercise 1.7

months = 1
principal = 500000
rate = 0.05
total_paid = 0
monthly_payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (monthly_payment + extra_payment)
        total_paid += monthly_payment + extra_payment
        if principal < 0:
            total_paid += principal
            principal = 0
    else:
        principal = principal * (1 + rate / 12) - monthly_payment
        total_paid += monthly_payment
        if principal < 0:
            total_paid += principal
            principal = 0
    print(
        f"Month {months} | Total paid:  {round(total_paid, 2)} | Remaining balance: {round(principal, 2)}"
    )
    months += 1
