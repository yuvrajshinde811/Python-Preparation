# Welcome to my Bank Project

class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Must be greater than zero.")
            return False
        self.balance += amount
        print(f"Deposited Rs. {amount:.2f}. New balance: Rs. {self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Must be greater than zero.")
            return False
        if amount > self.balance:
            print(f"Insufficient balance! Available: Rs. {self.balance:.2f}")
            return False
        self.balance -= amount
        print(f"Withdrawn Rs. {amount:.2f}. New balance: Rs. {self.balance:.2f}")
        return True

    def display(self):
        print("\n--- Account Details ---")
        print(f"  Name       : {self.name}")
        print(f"  Account No : {self.acc_no}")
        print(f"  Balance    : Rs. {self.balance:.2f}")
        print("-----------------------")


def get_int_input(prompt):
    """Safely get integer input from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_float_input(prompt):
    """Safely get float input from user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def get_account(accounts):
    """Prompt for account number and return account if found."""
    acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found!")
        return None
    return accounts[acc_no]


accounts = {}

while True:
    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Account")
    print("5. List All Accounts")
    print("6. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        acc_no = input("Enter account number: ").strip()
        if not acc_no:
            print("Account number cannot be empty.")
            continue
        if acc_no in accounts:
            print("Account already exists!")
        else:
            balance = get_float_input("Enter initial balance: ")
            if balance < 0:
                print("Initial balance cannot be negative.")
            else:
                accounts[acc_no] = BankAccount(name, acc_no, balance)
                print(f"Account '{acc_no}' created successfully!")

    elif choice == "2":
        account = get_account(accounts)
        if account:
            amount = get_float_input("Enter amount to deposit: ")
            account.deposit(amount)

    elif choice == "3":
        account = get_account(accounts)
        if account:
            amount = get_float_input("Enter amount to withdraw: ")
            account.withdraw(amount)

    elif choice == "4":
        account = get_account(accounts)
        if account:
            account.display()

    elif choice == "5":
        if not accounts:
            print("No accounts found.")
        else:
            print(f"\n{'Acc No':<15} {'Name':<20} {'Balance':>10}")
            print("-" * 47)
            for acc in accounts.values():
                print(f"{acc.acc_no:<15} {acc.name:<20} Rs. {acc.balance:>9.2f}")

    elif choice == "6":
        print("Thank you for using the Bank System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")