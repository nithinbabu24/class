from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year
    
    def calculate_years_on_platform(self):
        current_year = 2025
        return current_year - self.joining_year
    
    @abstractmethod
    def get_role(self):
        pass
    
    def __str__(self):
        years_on_platform = self.calculate_years_on_platform()
        return f"Name: {self.name}, Role: {self.get_role()}, Years on Platform: {years_on_platform}"

class Customer(User):
    def get_role(self):
        return "Customer"
    
    def __str__(self):
        years_on_platform = self.calculate_years_on_platform()
        return f"🌟 Customer Profile 🌟\nName: {self.name}\nRole: {self.get_role()}\nMember for: {years_on_platform} year(s)"

class Vendor(User):
    def get_role(self):
        return "Vendor"
    
    def __str__(self):
        years_on_platform = self.calculate_years_on_platform()
        return f"🏪 Vendor Profile 🏪\nName: {self.name}\nRole: {self.get_role()}\nPartner for: {years_on_platform} year(s)"


if __name__ == "__main__":
    
    customer1 = Customer("Alice Smith", 2022)
    vendor1 = Vendor("Bob's Electronics", 2019)
    customer2 = Customer("Charlie Brown", 2024)
    
    
    print("=== User Account System ===")
    print(customer1)
    print("\n" + "="*30 + "\n")
    print(vendor1)
    print("\n" + "="*30 + "\n")
    print(customer2)