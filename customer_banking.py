# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
import os
os.system('cls')

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Set your initial savings balance: "))
    savings_interest = float(input("Set your interest rate: "))    
    savings_maturity = int(input("Set length of months for you savings: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("----------------------------------------")
    print(f"Interest earned for {savings_maturity} months is: {interest_earned:,.2f} and your savings balance is: {updated_savings_balance:,.2f}")
    print("----------------------------------------")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("\nSet your CD balance: "))
    cd_interest = float(input("Set your CD interest rate: "))
    cd_maturity = int(input("Set length of months for your CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("----------------------------------------")
    print(f"Interest earned for {cd_maturity} months is: {interest_earned:,.2f} and your CD balance is: {updated_cd_balance:,.2f}")
    print("----------------------------------------")
    
if __name__ == "__main__":
    # Call the main function.
    main()
