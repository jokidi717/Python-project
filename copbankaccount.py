# The parent class BankAccount
class BankAccount:
    # Constructor method
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance  # Protected attribute (Encapsulation)

    # deposit() method
    def deposit(self, amount):
        """Allow deposit of money into the account to add to the balance."""
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive")

    # withdraw() method
    def withdraw(self, amount):
        """Allow withdrawal of money from the account to reduce the balance."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self._balance}")
        else:
            print("Insufficient funds or invalid amount.")
# Creating an instance of BankAccount
account = BankAccount("John Doe", 500)

# Testing deposit
account.deposit(200)      # Output: Deposited 200. New balance: 700

# Testing invalid deposit
account.deposit(-50)      # Output: Deposit amount must be positive

# Testing withdrawal
account.withdraw(100)     # Output: Withdrew 100. Remaining balance: 600

# Testing over-withdrawal
account.withdraw(1000)    # Output: Insufficient funds or invalid amount.
