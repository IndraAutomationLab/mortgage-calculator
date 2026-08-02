loan_amount = float(input("Loan amount: "))
annual_rate = float(input("Annual interest rate (%): "))
years = int(input("Loan term in years: "))
annual_property_tax = float(input("Annual property taxes: "))
annual_home_insurance = float(input("Annual homeowners insurance: "))

monthly_rate = annual_rate / 100 / 12
num_payments = years * 12

if monthly_rate == 0:
    principal_interest = loan_amount / num_payments
else:
    principal_interest = loan_amount * (
        monthly_rate /
        (1 - (1 + monthly_rate) ** (-num_payments))
    )

monthly_property_tax = annual_property_tax / 12
monthly_home_insurance = annual_home_insurance / 12

total_monthly_payment = (
    principal_interest
    + monthly_property_tax
    + monthly_home_insurance
)

print("\nMonthly payment breakdown")
print("-------------------------")
print(f"Principal and interest: ${principal_interest:,.2f}")
print(f"Property taxes:        ${monthly_property_tax:,.2f}")
print(f"Homeowners insurance:  ${monthly_home_insurance:,.2f}")
print("-------------------------")
print(f"Total monthly payment: ${total_monthly_payment:,.2f}")
