class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return f"{super().display_info()}, Number of Seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return f"{super().display_info()}, Cargo Capacity: {self.cargo_capacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"{super().display_info()}, Engine Capacity: {self.engine_capacity} cc"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle.display_info())

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle.display_info()
        return "Vehicle not found."

# Demonstration of functionalities

# Create Fleet instance
fleet = Fleet()

# Create Vehicle instances
car1 = Car("ABC123", "Toyota", "Camry", 5)
truck1 = Truck("XYZ789", "Ford", "F-150", 10)
motorcycle1 = Motorcycle("MNO456", "Yamaha", "YZF-R3", 321)

# Add vehicles to the fleet
fleet.add_vehicle(car1)
fleet.add_vehicle(truck1)
fleet.add_vehicle(motorcycle1)

# Display all vehicles
print("Displaying all vehicles:")
fleet.display_vehicles()

# Search for a vehicle by registration number
print("\nSearching for vehicle with registration number 'XYZ789':")
print(fleet.search_vehicle("XYZ789"))

print("\nSearching for vehicle with registration number 'ZZZ999':")
print(fleet.search_vehicle("ZZZ999"))
