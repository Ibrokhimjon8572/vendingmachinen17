from beverage import Beverage
from qator import Qator

class VendingMachine:
    def __init__(self) -> None:
        self.qator_list = [Qator(i) for i in range(1, 7)]

    def add_beverage(self, qator, beverage: Beverage):
        qator = self.qator_list[qator-1]
        return qator.add_beverage(beverage)

    def check(self, qator):
        qator = self.qator_list[qator-1]
        qator.getlist()


    def get_price(self, name):
        pass