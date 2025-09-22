
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")



class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")



class PartTime(Person):
    def __init__(self, name: str, age: int, working_hours: float):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")

class Consultant(Employee, PartTime):
    def __init__(self, name: str, age: int, employee_id: str, working_hours: float, project_name: str):
        
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, "
              f"Employee ID: {self.employee_id}, Working Hours: {self.working_hours}, "
              f"Project: {self.project_name}")



p1 = Person("Alice", 30)
e1 = Employee("Bob", 40, "E123")
pt1 = PartTime("Charlie", 25, 20.5)
c1 = Consultant("Diana", 35, "C456", 15.0, "AI Project")


p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()
