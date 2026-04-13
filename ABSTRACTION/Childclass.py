from abc import ABC,abstractmethod
class vechicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vechicle):
    def start(self):
        print("car starts with key")
class bike(vechicle):
    def start(self):
        print("bike starts with kick")
c=car()
c.start()
b=bike()
c.start()