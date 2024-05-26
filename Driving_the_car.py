class Car:

    def __init__(self, mileage: int, fuel: int, economy, color, model):
        self.mileage = mileage
        self.fuel = fuel
        self.economy = economy
        self.color = color
        self.model = model

    def drive(self, distance):
        fuel_enough_for_distance = distance / self.economy / 100
        if fuel_enough_for_distance > self.fuel:
            raise Exception ("Not enough fuel")
        else:
            self.mileage = self.mileage + distance
            self.fuel = self.fuel - fuel_enough_for_distance

    def distance_left(self):
        return self.fuel * self.economy

    def fuel_up(self):
        self.fuel = self.fuel + 20

import random
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Tesla", "Mitsubishi", "Mustang", "Volkswagen"]
colors = ["brown", "white", "yellow", "black", "blue"]
cars = []

for i in models:
    economy = random.randint(5, 30)
    color = random.choice(colors)
    model = random.choice(models)
    car = Car(0, 100, economy, color, model)
    cars.append(car)

for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

max_fuel_car = max(cars, key=lambda x: x.fuel)
print(f"Car with max fuel: {max_fuel_car.model}," f" {max_fuel_car.color}, mileage: {max_fuel_car.mileage},"
      f" fuel: {max_fuel_car.fuel}")




