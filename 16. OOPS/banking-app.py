"""
Banking
    Attributes - acc_no,name,account_type,balance,branch
    Methods - display(), 



Menu
1) Add a account
    acc_no = INT
    name = STR
    account_type = STR (saving/current)
    balance
    branch = STR
    x = Banking(acc_no,name,account_type,branch)
2) Display all account
    - All account display
3) Check Balance of a account
4) Deposit Balance
5) Withdraw money
6) Exit
"""

from typing import List


class Banking:
    def __init__(self, account_no, branch, name, account_Type):
        self.account_no: int = account_no
        self.branch: str = branch
        self.name: str = name
        self.account_Type: str = account_Type
        self.balance: int = 0

    def get_balance(self) -> int:
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Updated balance = {self.balance}\n\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuff balance")
            return
        self.balance -= amount
        print(f"Updated balance = {self.balance}\n\n")

    def display(self):
        print(f"Account No = {self.account_no}")
        print(f"Name = {self.name}")
        print(f"Account Type = {self.account_Type}")
        print(f"Balance = {self.balance}")
        print(f"Branch = {self.branch}")


accounts: List[Banking] = []


while True:
    print("1. Add account details")
    print("2. Display Account Details")
    print("3) Check Balance of a account")
    print("4) Deposit Balance")
    print("5) Withdraw money")

    print("6) Exit")

    choice = int(input("Enter your choice = "))
    if choice == 1:
        name = input("Enter your name : ")
        number = int(input("Enter your account number : "))
        branch = input("Enter your account branch : ")
        account_Type = input("Enter your account account_Type : ")
        x = Banking(number, branch, name, account_Type)
        accounts.append(x)
        # print(accounts)
    elif choice == 2:
        for acc in accounts:
            acc.display()
    elif choice == 3:
        acc_no = int(input("Enter account number = "))
        for acc in accounts:
            if acc.account_no == acc_no:
                print(f"Your balance is = {acc.get_balance()}")
    elif choice == 4:
        acc_no = int(input("Enter account number to deposit into = "))
        for acc in accounts:
            if acc.account_no == acc_no:
                amt = int(input("Enter amount to deposit = "))
                acc.deposit(amt)
                break
    elif choice == 5:
        acc_no = int(input("Enter account number to withdraw from = "))
        for acc in accounts:
            if acc.account_no == acc_no:
                amt = int(input("Enter amount to withdraw = "))
                acc.withdraw(amt)
                break
