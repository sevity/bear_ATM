class Bank:
    def __init__(self):
        self.accounts = {} # 계좌 정보

    def validate_pin(self, pin):
        # PIN 번호 확인 로직
        return True

    def get_account(self, account_id):
        return self.accounts.get(account_id, None)
