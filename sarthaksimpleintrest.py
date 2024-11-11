# Simple Interest Calculator

# Input values
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): "))
time = float(input("Enter time period (in years): "))

# Calculate simple interest
interest = (principal * rate * time) / 100

# Calculate total amount
amount = principal + interest

# Print results
print("Principal Amount: ", principal)
print("Interest Rate: ", rate, "%")
print("Time Period: ", time, "years")
print("Simple Interest: ", interest)
print("Total Amount: ", amount)


