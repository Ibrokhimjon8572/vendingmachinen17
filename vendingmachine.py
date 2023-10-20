from beverage import Beverage
from qator import Qator
from card import Card

class VendingMachine:
    def __init__(self) -> None:
        self.card_list: list[Card] = []
        self.qator_list = [Qator(i) for i in range(1, 7)]

    def assigne_card(self, card_id, summa):
        for card in self.card_list:
            if card._id == card_id and card.kredit < summa:
                return -1

    def available_cans(self, name):
        count = 0
        for qator in self.qator_list:
            ichimlik = qator.ichimlik
            if ichimlik == None:
                continue
            elif ichimlik.name == name:
                count += qator._number_beverage
        return count

    def add_beverage(self, qator, beverage: Beverage, number_beverage):
        qator = self.qator_list[qator-1]
        return qator.add_beverage(beverage, number_beverage)

    def info(self, qator):
        qator = self.qator_list[qator-1]
        return qator.getinfo()

    def get_price(self, name):
        for qator in self.qator_list:
            check = qator.get_price(name)
            if  check != None:
                return check
        return -1.0

    def get_credit(self, id):
        for card in self.card_list:
            if card._id == id:
                return card.kredit
        return -1.0

    def helper(self, card_id, ichimlik_narxi, nomi):
        for card in self.card_list:
            if card._id == card_id:
                card.spend_money(ichimlik_narxi)

        for qator in self.qator_list:
            if qator.ichimlik != None and qator.ichimlik.name == nomi:
                qator._number_beverage -= 1

    def sell(self, nomi, card_id):
        ichimlik_narxi = self.get_price(nomi)
        if ichimlik_narxi == -1.0:
            return -1.0
        elif self.get_credit(card_id) == -1.0:
            return -1.0
        elif self.assigne_card(card_id, ichimlik_narxi) == -1.0:
            return -1.0
        else:
            self.helper(card_id, ichimlik_narxi, nomi)
        

    def recharge_card(self, id, debit):
        for card in self.card_list:
            if card._id == id:
                card.add_summa(debit)
                print(f'{id} ga {debit} som qo\'shildi, {card.kretid}')
                return
        card = Card(id, debit)
        self.card_list.append(card)
        print('karta qo\'shildi')