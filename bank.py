from account import Account

class Bank:
    def __init__(self):
        self._accounts = {}
        self._cards = {} # 카드와 계정을 연결하기 위한 딕셔너리


    def add_account(self, card_number, account_number, account):
        self._accounts[account_number] = account
        if card_number in self._cards:
            self._cards[card_number].append(account_number)
        else:
            self._cards[card_number] = [account_number]

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
        # 카드 번호와 관련된 계정을 가져오는 로직
        return self._cards.get(card_number, [])
