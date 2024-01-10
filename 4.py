# Write a Python program to create a class representing a bank. Include methods for
# managing customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with an initial balance of ${initial_balance}.")
        else:
            print(f"Error: Account {account_number} already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount} deposited into account {account_number}. Current balance: ${self.accounts[account_number]}.")
        else:
            print(f"Error: Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount} withdrawn from account {account_number}. Current balance: ${self.accounts[account_number]}.")
            else:
                print(f"Error: Insufficient funds in account {account_number}.")
        else:
            print(f"Error: Account {account_number} does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Current balance in account {account_number}: ${self.accounts[account_number]}.")
        else:
            print(f"Error: Account {account_number} does not exist.")

# Example usage:
bank = Bank()

while True:
    print("\nBanking Operations:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        account_number = input("Enter the account number: ")
        initial_balance = float(input("Enter the initial balance: "))
        bank.create_account(account_number, initial_balance)
    elif choice == '2':
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to deposit: "))
        bank.deposit(account_number, amount)
    elif choice == '3':
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to withdraw: "))
        bank.withdraw(account_number, amount)
    elif choice == '4':
        account_number = input("Enter the account number: ")
        bank.check_balance(account_number)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
