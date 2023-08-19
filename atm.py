from bank import Bank
from card_reader import CardReader
from cash_bin import CashBin


class ATM:
    def __init__(self, bank, initial_cash_balance, cash_bin_capacity):
        self.bank = bank
        self.current_card = None
        self.current_accounts = None
        self.card_reader = CardReader() # 카드 리더 객체 생성
        self.cash_bin = CashBin(initial_cash_balance, cash_bin_capacity) # 현금함의 최대 저장치 설정


    def insert_card(self, card_number):
        if self.card_reader.insert_card(card_number):
            self.current_card = card_number
            return True
        return False
    
    def eject_card(self):
        self.current_card = None
        self.card_reader.eject_card()

    def check_pin(self, pin):
        return self.bank.validate_pin(pin)

    def select_accounts(self):
        self.current_accounts = self.bank.get_accounts(self.current_card)
        return self.current_accounts

    def balance(self, account_number):
        return self.bank.get_balance(account_number)

    def deposit(self, account_number, amount):
        success = self.cash_bin.deposit(amount) # 현금함에 먼저 입금 시도
        if success:
            success = self.bank.deposit(account_number, amount) # 성공하면 은행 계좌에 입금
        return success

    def withdraw(self, account_number, amount):
        success = self.bank.withdraw(account_number, amount)
        if success:
            success = self.cash_bin.withdraw(amount) # 현금함에서 출금
        return success