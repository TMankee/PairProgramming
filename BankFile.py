class BankAccount:
    customerName = ""
    accountNumber = 0
    balance = 0.00

    def __init__(self,a,b,c):
        self.customerName = a
        self.accountNumber = b
        self.balance = c

    def deposit(self):
        self.balance = self.balance + float(input("How much would you like to deposit? \n"))
    
    def withdraw(self):
        amount = float(input("How much would you like to withdrawl? \n"))
        if self.balance < amount:
            print("Error")
        else:
            self.balance = self.balance - amount

obj = BankAccount("Joe Bloggs",10000,100.00)

obj.deposit()
obj.withdraw()