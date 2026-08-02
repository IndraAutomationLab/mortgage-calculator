home_price = float(input("Home price: "))
down_payment_percent = float(input("Down payment (%): "))
annual_rate = float(input("Annual interest rate (%): "))
years = int(input("Loan term in years: "))
annual_property_tax = float(input("Annual property taxes: "))
annual_home_insurance = float(input("Annual homeowners insurance: "))

down_payment = home_price * (down_payment_percent / 100)
loan_amount = home_price - down_payment

if loan_amount <= 0:
    print("Error: Down payment must be less than the home price.")
    exit()

if years <= 0:
    print("Error: Loan term must be greater than zero.")
    exit()

monthly_rate = annual_rate / 100 / 12
num_payments = years * 12

if monthly_rate == 0:
    principal_and_interest = loan_amount / num_payments
    monthly_interest = 0
else:
    principal_and_interest = loan_amount * (
        monthly_rate /
        (1 - (1 + monthly_rate) ** (-num_payments))
    )
    monthly_interest = loan_amount * monthly_rate

monthly_principal = principal_and_interest - monthly_interest
monthly_property_tax = annual_property_tax / 12
monthly_home_insurance = annual_home_insurance / 12

monthly_escrow = monthly_property_tax + monthly_home_insurance
total_monthly_mortgage = principal_and_interest + monthly_escrow

print("\nMortgage summary")
print("---------------------------------")
print(f"Home price:             ${home_price:,.2f}")
print(f"Down payment:           ${down_payment:,.2f}")
print(f"Financed loan amount:   ${loan_amount:,.2f}")

print("\nFirst monthly payment breakdown")
print("---------------------------------")
print(f"Principal:              ${monthly_principal:,.2f}")
print(f"Interest:               ${monthly_interest:,.2f}")
print(f"Principal and interest: ${principal_and_interest:,.2f}")
print(f"Property taxes:         ${monthly_property_tax:,.2f}")
print(f"Homeowners insurance:   ${monthly_home_insurance:,.2f}")
print(f"Total escrow:           ${monthly_escrow:,.2f}")
print("---------------------------------")
print(f"Total monthly mortgage: ${total_monthly_mortgage:,.2f}")
