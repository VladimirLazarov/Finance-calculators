# finance_calculators.py
import math

# show the menu
print("Welcome to the Finance Calculator!")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Ask user to enter his choice 
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#  user's choice and  calculations accordingly
if user_choice == "investment":
    # ask user input for investment calculation
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Perform investment calculation
    if interest_type == "simple":
        total_amount = principal * (1 + interest_rate * years)
    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    # Print the result
    print(f"\nThe total amount after {years} years of {interest_type} interest is: {total_amount:.2f}")

elif user_choice == "bond":
    # ask for user input for bond calculation
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate: "))
    months = int(input("Enter the number of months to repay the bond: "))

    # Calculate monthly interest rate and perform bond repayment calculation
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    # Print the result
    print(f"\nThe monthly bond repayment amount is: {repayment:.2f}")

else:
    # Invalid choice to be printed 
    print("Invalid input. Please enter 'investment' or 'bond'.")