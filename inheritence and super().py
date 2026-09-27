# Topic: Inheritance and super()
# Advanced Back-End Development - Lecture 2

# Base / Parent Class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_brand(self):
        print(f"Vehicle Brand: {self.brand}, Manufacturing Year: {self.year}")

    def start_engine(self):
        print(f"The engine of {self.brand} is starting...")


# Derived / Child Class
class Car(Vehicle):
    def __init__(self, brand, model, year, doors=4):
        # super().__init__() invokes the parent class constructor
        super().__init__(brand, year)
        # Child-specific attribute
        self.model = model
        self.doors = doors

    # Child-specific method
    def show_full(self):
        print(f"Car Details: {self.brand} {self.model} ({self.year}) with {self.doors} doors")

    # Method Overriding: extending parent method behavior
    def start_engine(self):
        super().start_engine()
        print(f"Car {self.brand} {self.model} is ready to drive!")


# Another Derived / Child Class
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity_kwh):
        super().__init__(brand, model, year)
        self.battery_capacity_kwh = battery_capacity_kwh

    def show_battery(self):
        print(f"{self.brand} {self.model} has a {self.battery_capacity_kwh} kWh battery.")


if __name__ == '__main__':
    print("--- Vehicle Base Class ---")
    generic_vehicle = Vehicle("Toyota", 2020)
    generic_vehicle.show_brand()
    generic_vehicle.start_engine()

    print("\n--- Car Derived Class (Inheritance & super()) ---")
    my_car = Car("Ford", "Mustang", 2023, doors=2)
    my_car.show_brand()
    my_car.show_full()
    my_car.start_engine()

    print("\n--- ElectricCar Multi-level Inheritance ---")
    tesla = ElectricCar("Tesla", "Model 3", 2024, 75)
    tesla.show_brand()
    tesla.show_full()
    tesla.show_battery()
    tesla.start_engine()
