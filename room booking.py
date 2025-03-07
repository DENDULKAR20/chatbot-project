class RoomBookingBot:
    def __init__(self):
        self.rooms = {
            "Room 101": {"available": True, "price": 100},
            "Room 102": {"available": True, "price": 120},
            "Room 103": {"available": False, "price": 150},
            "Room 104": {"available": True, "price": 90},
        }

    def display_rooms(self):
        print("\nAvailable Rooms:")
        for room, details in self.rooms.items():
            status = "Available" if details["available"] else "Not Available"
            print(f"{room}: {status}, Price per night: ${details['price']}")

    def book_room(self, room_name):
        if room_name in self.rooms and self.rooms[room_name]["available"]:
            self.rooms[room_name]["available"] = False
            print(f"\n{room_name} has been successfully booked!")
        elif room_name in self.rooms:
            print(f"\nSorry, {room_name} is currently not available.")
        else:
            print("\nRoom not found. Please try again.")

    def check_availability(self):
        available_rooms = [room for room, details in self.rooms.items() if details["available"]]
        return available_rooms

    def start_chat(self):
        print("Welcome to our Hotel Denz!")
        while True:
            print("\nHow can I assist you My friend ?")
            print("1. Check available rooms")
            print("2. Book a room")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                available_rooms = self.check_availability()
                if available_rooms:
                    print("\nAvailable Rooms:", ", ".join(available_rooms))
                else:
                    print("\nNo rooms are currently available.")
            elif choice == "2":
                room_name = input("\nEnter the room name you want to book (e.g., Room 101): ")
                self.book_room(room_name)
            elif choice == "3":
                print("\nThank you for visit ,Be Happy!")
                break
            else:
                print("\nInvalid choice. Please try again.")

bot = RoomBookingBot()
bot.start_chat()
