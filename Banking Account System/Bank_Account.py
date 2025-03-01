class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def menu_driven(self):
        print("<--- BANKING ACCOUNT SYSTEM --->")
        print("----------------------------------------")
        print("Choose from the following Options given below:")
        print("Press 1 to Create an Account (Savings/Checking)")
        print("Press 2 to Deposit Money")
        print("Press 3 to Withdraw Money")
        print("Press 4 to Check Account Balance")
        print("Press 5 to Exit")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            input("Create your Bank Account: ")
            print("Your account has been created!")
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Exiting...")
        else:
            print("Invalid Input. Please Try Again!")

    def deposit(self):
        deposit_amount = int(input("Enter the amount to deposit: $"))
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"${deposit_amount} has been deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self):
        withdraw_amount = int(input("Enter the amount to withdraw: $"))
        if 0 < withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(
                f"${withdraw_amount} has been withdrawn. New balance: ${self.balance}"
            )
        else:
            print("Insufficient funds or invalid amount!")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def bank_account_details(self):
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        self.check_balance()  # Call function instead of printing None


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}")

    def saving_account_details(self):
        self.bank_account_details()
        print(f"Interest Rate: {self.interest_rate}%")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self):
        withdraw_amount = int(input("Enter the withdrawal amount: $"))
        if 0 < withdraw_amount <= (self.balance + self.overdraft_limit):
            self.balance -= withdraw_amount
            print(f"${withdraw_amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit!")

    def checking_account_details(self):
        self.bank_account_details()
        print(f"Overdraft Limit: ${self.overdraft_limit}")


# --- Testing ---
bank = CheckingAccount("123456", "Alice", 2000, 500)
bank.menu_driven()
bank.deposit()
bank.withdraw()
bank.check_balance()
bank.checking_account_details()

savings = SavingsAccount("67890", "Jenny", 2000, 3.5)
savings.apply_interest()
savings.saving_account_details()
