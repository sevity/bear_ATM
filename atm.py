from bank import Bank
from account import Account

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_account = None

    def insert_card(self, account_id, pin):
        if self.bank.validate_pin(pin):
            self.current_account = self.bank.get_account(account_id)
            return True
        else:
            return False

    def select_account(self, account_id):
        self.current_account = self.bank.get_account(account_id)

    def see_balance(self):
        return self.current_account.get_balance()

    def deposit(self, amount):
        self.current_account.deposit(amount)

    def withdraw(self, amount):
        return self.current_account.withdraw(amount)
