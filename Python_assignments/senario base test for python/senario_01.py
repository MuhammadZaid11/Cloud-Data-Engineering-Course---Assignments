senario_01

# Custom exception class
class InvalidGradeError(Exception):
    def __init__(self, student_name, grade):
        super().__init__(f"Invalid grade '{grade}' for student '{student_name}'")


def read_student_records(filename):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    name, grade = line.strip().split(",")
                    name = name.strip()
                    grade = grade.strip()

                    # Check if grade is numeric
                    if not grade.isdigit():
                        raise InvalidGradeError(name, grade)

                    students.append((name, int(grade)))

                except InvalidGradeError as e:
                    print("Error:", e)
                except ValueError:
                    print(f"Invalid line format: {line.strip()}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    return students


def calculate_average(students):
    if not students:
        return 0
    total = sum(grade for _, grade in students)
    return total / len(students)


# Main Program
if __name__ == "__main__":
    filename = "student_records.txt"
    student_data = read_student_records(filename)

    print("\nValid Student Records:")
    for name, grade in student_data:
        print(f"{name}: {grade}")

    avg = calculate_average(student_data)
    print(f"\nAverage Grade of Valid Students: {avg:.2f}")

"""# scenario_02"""

# Base Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.make} {self.model} engine started.")

    def stop_engine(self):
        print(f"{self.make} {self.model} engine stopped.")

    def display_info(self):
        print(f"--- Vehicle Information ---")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# Subclass: Car
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.doors}")

    def accelerate(self):
        print(f"{self.make} {self.model} is accelerating smoothly!")


# Subclass: Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity  # in tons

    def display_info(self):
        super().display_info()
        print(f"Cargo Capacity: {self.cargo_capacity} tons")

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            print(f"Loading {weight} tons of cargo into the truck.")
        else:
            print(f"Cannot load {weight} tons! Exceeds capacity of {self.cargo_capacity} tons.")


# Subclass: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, drive_type):
        super().__init__(make, model, year)
        self.drive_type = drive_type  # e.g., Chain, Shaft, or Belt

    def display_info(self):
        super().display_info()
        print(f"Drive Type: {self.drive_type}")

    def wheelie(self):
        print(f"{self.make} {self.model} is performing a wheelie!")


# Demonstration of Inheritance
# -----------------------------

# Create objects for each vehicle type
car = Car("Toyota", "Corolla", 2022, 4)
truck = Truck("Volvo", "FH16", 2021, 18)
motorcycle = Motorcycle("Yamaha", "MT-09", 2023, "Chain")

# Access common methods (from base class)
car.start_engine()
truck.start_engine()
motorcycle.start_engine()

print("\nDisplaying Vehicle Details:\n")
car.display_info()
truck.display_info()
motorcycle.display_info()

print("\nPerforming Specific Actions:\n")
car.accelerate()
truck.load_cargo(15)
motorcycle.wheelie()

# Stop all engines
print("\nStopping Engines:")
car.stop_engine()
truck.stop_engine()
motorcycle.stop_engine()

"""# scenario_03"""

