from account import Account

class Bank:
    def __init__(self):
        self._accounts = {} 

    def add_account(self, account_id, balance):
        self._accounts[account_id] = Account(balance)

    def validate_pin(self, pin):
        # PIN 번호 확인 로직
        return True

    def get_account(self, account_id):
        return self._accounts.get(account_id, None)
