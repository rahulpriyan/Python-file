class bankaccount:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
account=bankaccount("rahulpriyan",10000)
class bankaccount:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.__name
acc=bankaccount("rahulpriyan",10000)
print(acc.get_balance())
print(acc.get_name())
