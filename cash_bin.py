# cash_bin.py
class CashBin:
    def __init__(self, initial_balance, max_capacity):
        self.balance = initial_balance
        self.max_capacity = max_capacity

    def deposit(self, amount):
        if self.balance + amount > self.max_capacity: # 현금함의 최대 저장치 확인
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance