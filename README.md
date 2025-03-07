Concepts Used:
The project is written entirely in Python, making use of basic syntax, classes, and functions to simulate a room booking system.
The RoomBookingBot class is used to encapsulate the room booking logic, including available rooms, room status, and booking functionality.
The room details (such as availability and price) are stored in a dictionary for easy access and modification.
The chatbot interacts with the user through the command line interface, taking input from the user and providing appropriate responses.
The project uses basic control structures like if-else statements and loops (while loop) to drive the flow of the chatbot.
Working :
A dictionary holds details about rooms (name, availability, and price).
Example: "Room 101": {"available": True, "price": 100}.
The chatbot can show available rooms based on their availability status by checking the dictionary.
If a user selects a room, the chatbot checks if it's available. If so, it updates the room's availability to False, meaning the room is now booked.
The chatbot continuously asks the user what they want to do—check available rooms, book a room, or exit. It uses a while loop to keep the conversation going until the user decides to exit.
