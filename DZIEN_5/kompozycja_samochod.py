class Engine:
    def start(self):
        print("Uruchomienie silnika")

    def stop(self):
        print("Wyłączenie silnika")

class Wheel:
    def obracanie(self):
        print("koło się obraca")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]

    def start(self):
        print("uruchomienie samochodu")
        self.engine.start()

    def stop(self):
        print("zgaszenie samochodu")
        self.engine.stop()

    def drive(self):
        print("Samochód się porusza")
        for wheel in self.wheels:
            wheel.obracanie()


moj_samochod = Car()

moj_samochod.start()
moj_samochod.drive()
moj_samochod.stop()
