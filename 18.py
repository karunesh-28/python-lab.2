'''Create a conference room booking system with classes for rooms, reservations,
and users. Include methods for checking room availability, booking time slots, and
sending notifications.'''

from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = []

    def check_availability(self, start_time, end_time):
        for reservation in self.reservations:
            if start_time < reservation.end_time and end_time > reservation.start_time:
                return False  # Room is already booked during the requested time slot
        return True

    def book_room(self, user, start_time, end_time):
        if self.check_availability(start_time, end_time):
            reservation = Reservation(user, self, start_time, end_time)
            self.reservations.append(reservation)
            return reservation
        else:
            print(f"Room {self.room_number} is not available during the requested time slot.")
            return None

    def display_reservations(self):
        print(f"\nReservations for Room {self.room_number}:")
        for reservation in self.reservations:
            reservation.display_info()


class Reservation:
    def __init__(self, user, room, start_time, end_time):
        self.user = user
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

    def display_info(self):
        print(f"User: {self.user.name}, Room: {self.room.room_number}, "
              f"Start Time: {self.start_time}, End Time: {self.end_time}")


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

# Example usage:
room1 = Room("101", 10)
room2 = Room("102", 8)

user1 = User(1, "John Doe", "john@example.com")
user2 = User(2, "Jane Smith", "jane@example.com")

# Display available rooms
print("Available Rooms:")
print(f"Room {room1.room_number}, Capacity: {room1.capacity}")
print(f"Room {room2.room_number}, Capacity: {room2.capacity}")

# Book rooms for users
start_time1 = datetime(2022, 1, 15, 10, 0)  # January 15, 2022, 10:00 AM
end_time1 = datetime(2022, 1, 15, 12, 0)    # January 15, 2022, 12:00 PM

reservation1 = room1.book_room(user1, start_time1, end_time1)
if reservation1:
    print("\nReservation Successful!")
    reservation1.display_info()

start_time2 = datetime(2022, 1, 15, 11, 0)  # January 15, 2022, 11:00 AM
end_time2 = datetime(2022, 1, 15, 14, 0)    # January 15, 2022, 2:00 PM

reservation2 = room1.book_room(user2, start_time2, end_time2)
if reservation2:
    print("\nReservation Successful!")
    reservation2.display_info()

# Display reservations for rooms
room1.display_reservations()
room2.display_reservations()
