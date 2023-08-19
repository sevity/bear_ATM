import unittest
from atm import ATM
from bank import Bank
from account import Account

class TestATMController(unittest.TestCase):
    def setUp(self):  # 테스트 전 실행할 초기화 작업
        self.bank = Bank()
        self.bank.add_account('card1', '1234', Account(1000)) # 카드에 속한 계정 추가
        self.bank.add_account('card1', '5678', Account(2000))
        self.atm = ATM(self.bank, 1000, 3000) # 테스트용 ATM 객체 생성

    def test_insert_card(self): # 카드 삽입 테스트
        self.assertTrue(self.atm.insert_card('card1')) # 카드 검증이 항상 True라고 가정

    def test_select_account(self): # 계좌 선택 테스트
        self.atm.insert_card('card1')
        self.assertTrue(self.atm.check_pin('1111'))
        accounts = self.atm.select_accounts()
        self.assertIn('1234', accounts[0])

    def test_see_balance(self): # 잔액 확인 테스트
        self.atm.insert_card('card1')
        self.atm.check_pin('1111')
        accounts = self.atm.select_accounts()
        self.assertEqual(self.atm.balance(accounts[0]), 1000) # 초기 잔액과 일치해야 함

    def test_deposit(self): # 입금 테스트
        self.atm.insert_card('card1')
        self.atm.check_pin('1111')
        accounts = self.atm.select_accounts()
        self.assertTrue(self.atm.deposit(accounts[0], 500)) # 500 입금
        self.assertEqual(self.bank.get_balance(accounts[0]), 1500) # 최종 잔액 1500 확인

    def test_withdraw(self): # 출금 테스트
        self.atm.insert_card('card1')
        self.atm.check_pin('1111')
        accounts = self.atm.select_accounts()
        success = self.atm.withdraw(accounts[0], 300) # 300 출금
        self.assertTrue(success) # 출금 성공 확인
        self.assertEqual(self.bank.get_balance(accounts[0]), 700) # 최종 잔액 700 확인

    def test_deposit_exceeding_cash_bin_capacity(self): # 현금함 최대치 초과 입금 테스트
        self.atm.insert_card('card1')
        self.atm.check_pin('1111')
        accounts = self.atm.select_accounts()
        success = self.atm.deposit(accounts[0], 2500) # 현금함 최대 저장치 초과로 2500 입금 시도
        self.assertFalse(success) # 입금 실패 확인
        self.assertEqual(self.bank.get_balance(accounts[0]), 1000) # 초기 잔액과 일치해야 함

    def test_withdraw_insufficient_cash_bin_balance(self): # 현금함 잔액 부족 출금 테스트
        self.atm.insert_card('card1')
        self.atm.check_pin('1111')
        accounts = self.atm.select_accounts()
        success = self.atm.withdraw(accounts[0], 20000) # 현금함 잔액 부족 테스트
        self.assertFalse(success) # 출금 실패 확인
        self.assertEqual(self.bank.get_balance(accounts[0]), 1000) # 초기 잔액과 일치해야 함
if __name__ == "__main__":
    unittest.main()
