class bankaccount:
    def account(self):
        print("savingsaccount")
class premium(bankaccount):
    def premium(self):
        print("premium account-19000")
class savings(bankaccount):
    def savings(self):
        print("savings account-199990")
class currentaccount(premium,savings):
    def currentaccount(self):
        print("currentaccount-2000")
a=premium()
b=savings()
c=currentaccount()
a.account()
b.savings()
b.account()
c.account()
c.savings()
c.currentaccount()
