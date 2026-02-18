def simulate_loan(loan_amount, interest_rate, monthly_payment):
    months = 0
    balance = loan_amount

    while balance > 0:
        interest = balance * (interest_rate / 100) / 12
        balance = balance + interest - monthly_payment
        months += 1

        if balance <= 0:
            break

    return months

loan = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
payment = float(input("Enter monthly payment: "))

months_needed = simulate_loan(loan, rate, payment)

print("Loan paid off in", months_needed, "months.")
