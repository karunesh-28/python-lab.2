'''Build a simulation of an ATM system with classes for accounts, transactions, and
users. Implement methods for withdrawing cash, checking balances, and handling
PIN verification.'''

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Invalid amount or insufficient funds.")
            return False


class Transaction:
    @staticmethod
    def verify_pin(user_pin, entered_pin):
        return user_pin == entered_pin


class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account


# ATM simulation
def atm_system():
    # Creating a sample account
    user_account = Account(account_number="123456789", pin="1234", balance=1000)
    user = User(name="John Doe", account=user_account)

    while True:
        print("\nWelcome to the ATM, {}".format(user.name))
        entered_pin = input("Please enter your PIN: ")

        if Transaction.verify_pin(user.account.pin, entered_pin):
            print("PIN Verified.")

            while True:
                print("\n1. Check Balance\n2. Withdraw Cash\n3. Exit")
                choice = input("Enter your choice (1/2/3): ")

                if choice == "1":
                    print("Your balance is ${}".format(user.account.check_balance()))

                elif choice == "2":
                    amount = float(input("Enter the amount to withdraw: $"))
                    if user.account.withdraw_cash(amount):
                        print("Withdrawal successful. Remaining balance: ${}".format(user.account.balance))

                elif choice == "3":
                    print("Thank you for using the ATM. Goodbye!")
                    return

                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")

        else:
            print("Incorrect PIN. Please try again.")


if __name__ == "__main__":
    atm_system()
