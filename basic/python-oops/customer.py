import sys


class Customer:
    """Customer class for bank related operation"""
    bankName = "MYBANK"

    def __int__(self, name, amount=0):
        self.name = name
        self.amount = amount

    def withdraw(self, withdrawAmount):
        if self.amount < withdrawAmount:
            print("Insufficient fund")
            sys.exit()
        else:
            self.amount = self.amount - withdrawAmount
            print("Withdraw success\n Current balance : " + self.amount)

    def deposit(self, depositAmount):
        self.amount = self.amount + depositAmount


name = input('Enter Your name')
customer = Customer();
print("Welcome to ", customer.bankName)

while True:
    print('d-Deposite\nw-Withdraw\ne-Exit')
    option = input("Choose your option")
    if option == 'd' or option == 'D':
        amt = float(input('Enter the amount to deposit'))
        customer.deposit(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('Enter the amount to withdraw'))
        customer.withdraw(amt)
    elif option == 'e' or option == 'E':
        print("Thanks for the banking")
        sys.exit()
    else:
        print("Choose a valid option")
