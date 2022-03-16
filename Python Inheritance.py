class Car():
    def __init__(self, carname, enginetype, mileage):
        self.carname = carname
        self.enginetype = enginetype
        self.mileage = mileage

    def car_details(self):
        print("Car name is ", self.carname)
        print("Car Engine type is ", self.enginetype)
        print("Car mileage is ", self.mileage)


class Van(Car):
    def __init__(self, carname, enginetype, mileage, speed, gearbox):
        self.speed = speed
        self.gearbox = gearbox
        Car.__init__(self, carname, enginetype, mileage)

    def van_details(self):
        print("Car name is ", self.carname)
        print("Car Engine type is ", self.enginetype)
        print("Car mileage is ", self.mileage)
        print("Van speed is ", self.speed)
        print("Van Gearbox is ", self.gearbox)


c1 = Car("Audi", "Diesel", 18)
c1.car_details()

c2 = Car("Indica", "Petrol", 23, )
c2.car_details()

v1 = Van("Dezire", "diesel", 57, 90, 5)
v1.van_details()
print(c1)
print(c2)
print(v1)
