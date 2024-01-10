'''Build a hotel reservation system with classes for rooms, guests, and reservations.
Implement methods for checking room availability, booking rooms, and generating
invoices.'''

from datetime import date

class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_reserved = False

    def display_info(self):
        print(f"Room {self.room_number} - Capacity: {self.capacity}, Price per Night: ${self.price_per_night}")

    def is_available(self):
        return not self.is_reserved

    def reserve_room(self):
        if self.is_available():
            self.is_reserved = True
            return True
        else:
            print("Sorry, the room is not available.")
            return False


class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        print(f"Guest: {self.name}, Email: {self.email}, Phone: {self.phone}")


class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def generate_invoice(self):
        nights = (self.check_out_date - self.check_in_date).days
        total_cost = nights * self.room.price_per_night
        print(f"\nInvoice for {self.guest.name}:")
        print(f"Room: {self.room.room_number}, Nights: {nights}, Total Cost: ${total_cost}")


class HotelReservationSystem:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def check_room_availability(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.is_available()
        return False

    def book_room(self, guest, room_number, check_in_date, check_out_date):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.reserve_room():
                    reservation = Reservation(guest, room, check_in_date, check_out_date)
                    self.reservations.append(reservation)
                    print(f"\nReservation successful for Room {room.room_number}")
                    return
        print(f"Room {room_number} not found or not available for reservation.")

    def display_rooms_info(self):
        print("\nRooms Information:")
        for room in self.rooms:
            room.display_info()

    def display_guests_info(self):
        print("\nGuests Information:")
        for guest in self.guests:
            guest.display_info()

    def display_reservations_info(self):
        print("\nReservations Information:")
        for reservation in self.reservations:
            reservation.generate_invoice()


# Example usage:
hotel = HotelReservationSystem()

# Adding rooms to the hotel
room1 = Room(101, 2, 100)
room2 = Room(102, 4, 150)
room3 = Room(103, 3, 120)

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Adding guests to the hotel
guest1 = Guest("John Doe", "john@example.com", "123-456-7890")
guest2 = Guest("Jane Smith", "jane@example.com", "987-654-3210")

hotel.add_guest(guest1)
hotel.add_guest(guest2)

# Displaying rooms and guests information
hotel.display_rooms_info()
hotel.display_guests_info()

# Booking rooms
hotel.book_room(guest1, 101, check_in_date=date(2022, 1, 1), check_out_date=date(2022, 1, 5))
hotel.book_room(guest2, 102, check_in_date=date(2022, 2, 1), check_out_date=date(2022, 2, 5))

# Displaying reservations information and generating invoices
hotel.display_reservations_info()
