from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def start(self):
        pass

class UPI(Payment):
    def start(self):
        print("mode of payment: UPI")

class CreditCard(Payment):
    def start(self):
        print("mode of payment: creditcard")

class DebitCard(Payment):
    def start(self):
        print("mode of payment: debitcard")

s = UPI()
s.start()

c = CreditCard()
c.start()

d = DebitCard()
d.start()