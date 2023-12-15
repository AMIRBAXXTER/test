class BankAccount:
    number = 999
    accountnumbers = []

    def __init__(self, first_name, last_name, balance=0):
        self.firstname = first_name
        self.lastname = last_name
        self.accountnumber = BankAccount.number
        self.balance = balance
        BankAccount.accountnumbers.append(BankAccount.number)
        if BankAccount.number in BankAccount.accountnumbers:
            BankAccount.number += 1

    def display_balance(self):
        print(10 * "-", 10 * "=", 10 * "-")
        print(f"dear {self.firstname}\nyour balance is : {self.balance} rials")
        print(10 * "-", 10 * "=", 10 * "-")

    def dposit(self, amount: float = 0):
        amount = float(input("enter your amount:"))
        self.balance += amount
        self.display_balance()

    def withdraw(self, amount: float = 0):
        amount = float(input("enter your amount:"))
        if amount > self.balance:
            print(20 * "*")
            print("**Invalid request***")
            print(20 * "*")
        else:
            self.balance -= amount
        self.display_balance()


def atm(a=None):
    while True:
        choose = int(input(f"hi dear {a.firstname} {a.lastname} \naccount:[{a.accountnumber}] \nplease choose a "
                           f"option\n1-display balance\n2-deposit\n3-withdraw\n4-exit\nyour choose:"))
        if choose == 1:
            a.display_balance()
        elif choose == 2:
            a.dposit()
        elif choose == 3:
            a.withdraw()
        elif choose == 4:
            break
        else:
            print("Invalid choose")


if __name__ == "main":
    atm()
