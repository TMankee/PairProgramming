class BankAccount:
    customerName = ""
    accountNumber = 0
    balance = 0.00

    def __init__(self,a,b,c):
        self.customerName = a
        self.accountNumber = b
        self.balance = c

    def deposit(self):
        self.balance = self.balance + 