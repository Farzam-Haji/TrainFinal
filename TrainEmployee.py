from test1 import start_panel

class TrainLine:
    def __init__(self, name, start, end, stations):
        self.name = name
        self.start = start
        self.end = end
        self.stations = stations

    def update_line(self, start=None, end=None, stations=None):
        if start:
            self.start = start
        if end:
            self.end = end
        if stations:
            self.stations = stations

    def __str__(self):
        return f"Line: {self.name}, Start: {self.start}, End: {self.end}, Stations: {', '.join(self.stations)}"

class Train:
    def __init__(self, train_id, name, line, avg_speed, stop_duration, quality, ticket_price, capacity):
        self.train_id = train_id
        self.name = name
        self.line = line
        self.avg_speed = avg_speed
        self.stop_duration = stop_duration
        self.quality = quality
        self.ticket_price = ticket_price
        self.capacity = capacity

    def __str__(self):
        return f"Train {self.name} (ID: {self.train_id}), Line: {self.line}, Avg Speed: {self.avg_speed}, Capacity: {self.capacity}"

class TrainEmployee:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.train_lines = {}
        self.trains = {}

    def login(self, username, password):
        return self.username == username and self.password == password

    def add_train_line(self):
        line_name = input("Line name: ")
        if line_name in self.train_lines:
            print("Line already exists.")
        else:
            start = input("Start station: ")
            end = input("End station: ")
            stations = [input(f"Station {i+1}: ") for i in range(int(input("Number of stations: ")))]
            self.train_lines[line_name] = TrainLine(line_name, start, end, stations)
            print(f"Line '{line_name}' added.")

    def update_train_line(self):
        line_name = input("Line name to update: ")
        if line_name in self.train_lines:
            line = self.train_lines[line_name]
            print(f"Current details: {line}")
            field = input("Update (start/end/stations): ")
            if field == "start":
                line.update_line(start=input("New start: "))
            elif field == "end":
                line.update_line(end=input("New end: "))
            elif field == "stations":
                stations = [input(f"Station {i+1}: ") for i in range(int(input("Number of stations: ")))]
                line.update_line(stations=stations)
            print("Line updated.")
        else:
            print("Line not found.")

    def delete_train_line(self):
        line_name = input("Line name to delete: ")
        if line_name in self.train_lines:
            del self.train_lines[line_name]
            print(f"Line '{line_name}' deleted.")
        else:
            print("Line not found.")

    def view_train_lines(self):
        if self.train_lines:
            for line in self.train_lines.values():
                print(line)
        else:
            print("No lines found.")

    def employee_panel(self):
        while True:
            print("\n1. Add Line\n2. Update Line\n3. Delete Line\n4. View Lines\n5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_train_line()
            elif choice == '2':
                self.update_train_line()
            elif choice == '3':
                self.delete_train_line()
            elif choice == '4':
                self.view_train_lines()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")

    def add_train(self):
        train_id = input("Enter train ID: ")
        if train_id in self.trains:
            print("This train ID already exists. Please enter a unique ID.")
        else:
            name = input("Enter train name: ")
            line = input("Enter the train's line: ")
            if line not in self.train_lines:
                print(f"Line '{line}' does not exist. Please add the line first.")
                return
            avg_speed = input("Enter average speed: ")
            stop_duration = input("Enter stop duration at stations: ")
            quality = input("Enter train quality: ")
            ticket_price = input("Enter ticket price: ")
            capacity = int(input("Enter train capacity: ")) #edit
            self.trains[train_id] = Train(train_id, name, line, avg_speed, stop_duration, quality, ticket_price, capacity)
            print(f"Train '{name}' added successfully.")

    def delete_train(self):
        train_id = input("Enter the train ID to delete: ")
        if train_id in self.trains:
            del self.trains[train_id]
            print(f"Train '{train_id}' deleted successfully.")
        else:
            print("This train does not exist.")

    def view_trains(self):
        if self.trains:
            for train in self.trains.values():
                print(train)
        else:
            print("No trains available.")

    def employee_panel(self):
        while True:
            print("\n1. Add Train Line")
            print("2. Update Train Line")
            print("3. Delete Train Line")
            print("4. View Train Lines")
            print("5. Add Train")
            print("6. Delete Train")
            print("7. View Trains")
            print("8. Log Out")

            choice = input("Choose an option: ")

            if choice == '1':
                self.add_train_line()
            elif choice == '2':
                self.update_train_line()
            elif choice == '3':
                self.delete_train_line()
            elif choice == '4':
                self.view_train_lines()
            elif choice == '5':
                self.add_train()
            elif choice == '6':
                self.delete_train()
            elif choice == '7':
                self.view_trains()
            elif choice == '8':
                start_panel()
                break
            else:
                print("Invalid choice. Please try again.")

employee = TrainEmployee("John", "Doe", "john@example.com", "johndoe", "password123")

def main():
    # employee = TrainEmployee("John", "Doe", "john@example.com", "johndoe", "password123")

    while True:
        username = input("Username: ")
        password = input("Password: ")
        if employee.login(username, password):
            print(f"Welcome {employee.first_name} {employee.last_name}!")
            employee.employee_panel()
            break
        else:
            print("Incorrect username or password.")


main()
