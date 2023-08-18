import unittest
from atm import ATM
from bank import Bank
from account import Account

class TestATMController(unittest.TestCase):
    def setUp(self):  # 테스트 전 실행할 초기화 작업
        self.bank = Bank()
        self.bank.accounts = {
            '1234': Account(1000), # 두 개의 테스트 계좌 생성
            '5678': Account(2000)
        }
        self.atm = ATM(self.bank) # 테스트용 ATM 객체 생성

    def test_insert_card(self): # 카드 삽입 테스트
        self.assertTrue(self.atm.insert_card('1234', '1111')) # PIN 검증이 항상 True라고 가정

    def test_select_account(self): # 계좌 선택 테스트
        self.atm.insert_card('1234', '1111')
        self.atm.select_account('1234')
        self.assertEqual(self.atm.current_account, self.bank.accounts['1234'])

    def test_see_balance(self): # 잔액 확인 테스트
        self.atm.insert_card('1234', '1111')
        self.atm.select_account('1234')
        self.assertEqual(self.atm.see_balance(), 1000) # 초기 잔액과 일치해야 함

    def test_deposit(self): # 입금 테스트
        self.atm.insert_card('1234', '1111')
        self.atm.select_account('1234')
        self.atm.deposit(500) # 500 입금
        self.assertEqual(self.atm.current_account.get_balance(), 1500) # 최종 잔액 1500 확인

    def test_withdraw(self): # 출금 테스트
        self.atm.insert_card('1234', '1111')
        self.atm.select_account('1234')
        success = self.atm.withdraw(300) # 300 출금
        self.assertTrue(success) # 출금 성공 확인
        self.assertEqual(self.atm.current_account.get_balance(), 700) # 최종 잔액 700 확인

if __name__ == "__main__":
    unittest.main() 
