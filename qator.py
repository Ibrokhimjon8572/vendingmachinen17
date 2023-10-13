from beverage import Beverage

class Qator:
    def __init__(self, number) -> None:
        self._number = number
        self._name = ''
        self._ichimliklist: list[Beverage] = []

    def add_beverage(self, beverage: Beverage):
        # if self._name == beverage.name:
        self._name = beverage.name
        self._ichimliklist.append(beverage)
        return 'qo\'shildi'
        # return 'qo\'sha olmadim'
    
    def getlist(self):
        for i in self._ichimliklist:
            print(i.name, '-->', i.price)


    