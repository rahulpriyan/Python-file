class device:
    def power(self):
        print("the power of device is 190")
class laptop(device):
    def coding(self):
        print("python laguage")
class mobile(device):
    def call(self):
        print("vodafone offers a limited data network")
l=laptop()
m=mobile()
l.power()
l.coding()
l.power()
m.call()