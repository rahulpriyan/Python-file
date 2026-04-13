class car:
    def __init__(self,speed,fuel):
        self._speed=speed 
        self._fuel=fuel
        
    def get_speed(self):
        return self._speed
    def set_speed(self,speed):
        if 0<=speed<=200:
            self._speed=speed
        else:
            print("invalid speed")
    def __fuel_efficiency(self):
        return self._speed / 10
    def show_efficiency(self):
        print(f"Fuel efficiency:{self.__fuel_efficiency()} km/1")
car1=car(100,50)
car1.show_efficiency()
car1.set_speed(150)
car1.show_efficiency()
car1.set_speed(250)
print("Fuel level:",car1._Fuel_level)
