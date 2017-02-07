class BankAccount:
    def deposit(account):
        pass
    def withdraw(account):
        pass

class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500
        minimumbalance = 500

    def deposit(amount):
        if type(amount) != int or type(amount) != float:
            if amount<0:
                return "Invalid deposit amount"
            else:
                self.balance+=amount
                return self.balance
        else:
            return "Invalid Amount"

    def withdraw(amount):
        if type(amount) != int or type(amount) != float:
            if amount<0:
                return "Invalid withdraw amount"
            elif amount> self.balance:
                return "Cannot withdraw beyond the current account balanc"
            elif self.balance-amount < minimumbalance:
                return "Cannot withdraw beyond the minimum account balance"
            else:
                self.balance -=self.balance
                return self.balance
        else:
            return "Invalid Amount"
            
class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(amount):
        if type(amount) != int or type(amount) != float:
            
            if amount<0:
                return "Invalid deposit amount"
            else:
                self.balance+=amount
                return self.balance
        else:
            return "Invalid Amount"
    

    def withdraw(amount):
        if type(amount) != int or type(amount) != float:
            
            if amount<0:
                return "Invalid withdraw amount"
            elif amount> self.balance:
                return "Cannot withdraw beyond the current account balanc"
            else:
                self.balance -=balance
                return self.balance
        else:
            return "Invalid Amount"
