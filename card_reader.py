# card_reader.py
class CardReader:
    def __init__(self):
        self.current_card = None

    def insert_card(self, card_number):
        self.current_card = card_number
        return True

    def eject_card(self):
        self.current_card = None