class vehicle:
    def brand_vehicle(self):
        print("brand of the vechile:swift")
class car(vehicle):
    def model_car(self):
        print("model of the car:0995")
class sportscar(car):
    def speed_sportscar(self):
        print("speed of the sports car:190km")
c=sportscar()
c.brand_vehicle()
c.model_car()
c.speed_sportscar()