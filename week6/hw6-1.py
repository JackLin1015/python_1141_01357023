class vehicle:
    def __init__(self, name, year):
        self.name = name
        self.year = year

class car(vehicle):
    def __init__(self, name, year, seat):
        super().__init__(name, year)
        self.seat = seat
    def show(self):
        print(f"Car: {self.name}, Year: {self.year}, Seat: {self.seat}")

class motorcycle(vehicle):
    def __init__(self, name, year, cc):
        super().__init__(name, year)
        self.cc = cc
    def show(self):
        print(f"Motorcycle: {self.name}, Year: {self.year}, cc: {self.cc}")

class bike(vehicle):
    def __init__(self, name, year, model):
        super().__init__(name, year)
        self.model = model
    def show(self):
        print(f"Bicycle: {self.name}, Year: {self.year}, Model: {self.model}")

ans = []

while True:
    data = input().split()
    if not data:
        continue
    if data[0] == "Car":
        ans.append(car(data[1], data[2], data[3]))
    elif data[0] == "Motorcycle":
        ans.append(motorcycle(data[1], data[2], data[3]))
    elif data[0] == "Bicycle":
        ans.append(bike(data[1], data[2], data[3]))
    elif data[0] == "print":
        for j in ans:
            j.show()
    elif data[0] == "stop":
        break
