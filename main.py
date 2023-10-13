from vendingmachine import VendingMachine
from beverage import Beverage


machine = VendingMachine()

cola1 = Beverage('cola', 11000)

print(machine.add_beverage(1, cola1))

cola2 = Beverage('cola1.5', 18000)

print(machine.add_beverage(1, cola2))

machine.check(1)
