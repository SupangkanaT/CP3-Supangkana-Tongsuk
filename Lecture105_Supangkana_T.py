class Vahicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn On Air")

class Car(Vahicle):
    def sayHello(self):
        print("Hello world")

class PickUp(Vahicle):
    pass

class Van(Vahicle):
    pass

class EstateCar(Vahicle):
    pass

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()

car1 = Car()
car1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estateCar = EstateCar()
estateCar.turnOnAirConditioner()