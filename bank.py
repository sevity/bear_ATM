from account import Account

class Bank:
    def __init__(self):
        self._accounts = {}

    def add_account(self, account_number, account):
        self._accounts[account_number] = account

    def validate_pin(self, pin):
        # PIN 번호 확인 로직
        return True

    def get_balance(self, account_number):
        return self._accounts[account_number].get_balance()

    def deposit(self, account_number, amount):
        return self._accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        return self._accounts[account_number].withdraw(amount)

    def get_accounts(self, card_number):
        # 카드 번호와 관련된 계정을 가져오는 로직 (예: 딕셔너리 또는 데이터베이스 조회)
        return ['1234', '5678']
