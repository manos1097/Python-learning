class BankAccounts():

    def __init__(self):
        self.accountsList = []

    def showAccounts(self):
            print(self.accountsList)

    def getNewAccountId(self):
        if len(self.accountsList) == 0:
            return 1
        else:
            return len(self.accountsList) + 1

    def addAccount(self, firstname, lastname, balance=0):
        accountDetails = {
            'id': self.getNewAccountId(),
            'firstname': firstname,
            'lastname': lastname,
            'balance': balance
        }
        self.accountsList.append(accountDetails)

class Account():

    def __init__(self):
        self.id = 1
        self.balance = 0
        self.firstname = ''
        self.lastname = ''

    def deposit(self, account_id, amount_to_deposit):
        self.balance += amount_to_deposit
        print(f'Deposited {amount_to_deposit} $')

    def withdraw(self, account_id, amount_to_withdraw):
        if amount_to_withdraw <= self.balance:
            self.balance -= amount_to_withdraw

    def showBalance(self):
        print(f'Current balance is: {self.balance}')

bankAccounts = BankAccounts()
bankAccounts.addAccount('Manolis', 'Zaimakis', 5000)
bankAccounts.addAccount('Giannis', 'Zaimakis', 4000)
bankAccounts.addAccount('Fotini', 'Brachou', 6000)
bankAccounts.showAccounts()
