
class Vehicle:
    def __init__(self, vehicle_id: str, base_rate: float):
        self._vehicle_id = vehicle_id   
        self._base_rate = base_rate     

    def display_details(self) -> str:
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate:.2f}"

    def rental_charge(self) -> float:
        
        return 0.0



class Car(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, num_seats: int):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self) -> float:
        return self._base_rate * self.num_seats

    def display_details(self) -> str:
        return f"{super().display_details()}, Seats: {self.num_seats}"



class Bike(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, bike_type: str):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self) -> float:
        return self._base_rate * 0.5

    def display_details(self) -> str:
        return f"{super().display_details()}, Type: {self.bike_type}"


def calculate_rental(vehicle: Vehicle) -> float:
    return vehicle.rental_charge()



if __name__ == "__main__":
    car1 = Car("CAR001", 100.0, 4)
    bike1 = Bike("BIKE001", 50.0, "Scooter")

    print(car1.display_details())
    print("Rental Charge:", calculate_rental(car1))

    print(bike1.display_details())
    print("Rental Charge:", calculate_rental(bike1))
