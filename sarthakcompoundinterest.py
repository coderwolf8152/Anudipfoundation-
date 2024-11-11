# Compound Interest Calculator

# Input values
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): "))
time = float(input("Enter time period (in years): "))
n = int(input("Enter no of times interest applied per time period (n): "))

# Calculate compound interest
amount = principal * ((1 + rate / (100 * n)) ** (n * time))

# Calculate compound interest
interest = amount - principal

# Print results
print("Principal Amount: ", principal)
print("Interest Rate: ", rate, "%")
print("Time Period: ", time, "years")
print("No of times interest applied per time period (n): ", n)
print("Compound Interest: ", interest)
print("Total Amount: ", amount)

