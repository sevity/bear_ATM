from bank import Bank

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_card = None
        self.current_accounts = None

    def insert_card(self, card_number):
        self.current_card = card_number
        return True

    def check_pin(self, pin):
        return self.bank.validate_pin(pin)

    def select_accounts(self):
        self.current_accounts = self.bank.get_accounts(self.current_card)
        return self.current_accounts

    def balance(self, account_number):
        return self.bank.get_balance(account_number)

    def deposit(self, account_number, amount):
        return self.bank.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        return self.bank.withdraw(account_number, amount)
