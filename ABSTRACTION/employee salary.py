from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def start(self):
        pass

class Developer(employee):
    def start(self):
        print("mode of salary:developer")

class manager(employee):
    def start(self):
        print("mode of salary:manager")

s = Developer()
s.start()

c = manager()
c.start()

