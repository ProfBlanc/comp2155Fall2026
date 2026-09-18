"""
A motel reservation script

app will store room reservations for 5 rooms
each room will have
    room number
    price per night
    start date  (1-31)
    end date    (1-31)
    guess_name
A customer/guess can
    reserve a room from start date to end date
    checkout of room
        a bill is calculated
The app
    check to see which rooms are available
        empty or NOT during start and end date
            randomly assign room
                add guess name to room
        removes guess reservations from past

"""
import random

# create any needed variables
rooms: list[dict[str, str | int | float | None ]] = [
    {
        "room_number": 101,
        "price": 100.00,
        "guest": None,
        "start_date": None,
        "end_date": None,
    },
    {
        "room_number": 102,
        "price": 120.00,
        "guest": None,
        "start_date": None,
        "end_date": None,
    },
    {
        "room_number": 103,
        "price": 130.00,
        "guest": None,
        "start_date": None,
        "end_date": None,
    },
    {
        "room_number": 104,
        "price": 140.00,
        "guest": None,
        "start_date": None,
        "end_date": None,
    },
    {
        "room_number": 105,
        "price": 150.00,
        "guest": None,
        "start_date": None,
        "end_date": None,
    },

]

# your turn. add 5 entries to the rooms variable

# key = 'guess_name', value = 'john'
# key = 'room_num', value = 101
# key = 'price', value = 199.99

# create any needed functions

def display_rooms():
    # room number, price
    # status: available or occupied
    # if occupied, display occupied dates
    for room in rooms:
        print("Room number", room["room_number"])
        print("Price", room["price"])
        # determine if room is available?
        if room['guest'] is None:
            print("Status: Available")
        else:
            print("Status: Occupied by", room['guest'])
            print("From", room['start_date'], "to", room['end_date'])
        print("*" * 20)

def remove_guest_reservations_from_past(start):

    for room in rooms:
        if room['end_date'] is not None and room['end_date'] < start:
            checkout(room['room_number'])
            room['guest'] = None
            room['start_date'] = None
            room['end_date'] = None


def check_room_availability(start):
    # what should this return?
    # a single value or a collection of values?
        # collection: rooms where start and end date are blank
    remove_guest_reservations_from_past(start)
    available_rooms = []

    for room in rooms:
        if room['start_date'] is None and room['end_date'] is None and room['guest'] is None:
            available_rooms.append(room)
    return available_rooms

def reserve_room(guest, start, end):
    available_rooms = check_room_availability(start)
    random_room = random.choice(available_rooms)
    random_room['guest'] = guest
    random_room['start_date'] = start
    random_room['end_date'] = end


def checkout(room_number):
    for room in rooms:
        if room['room_number'] == room_number \
                and room['guest'] is not None :

            num_nights = room['end_date'] - room['start_date']
            sub_total = room['price'] * num_nights
            tax = sub_total * 0.13
            grand_total = sub_total + tax

            print("Guest", room['guest'], "that stay from",
                  room['start_date'], "to", room['end_date'], "checkout out")
            print("Stayed", num_nights, "nights")
            print("Sub Total", sub_total)
            print("Tax", tax)
            print("Grand Total", grand_total)
            break

# say 1st person reserves room from 1-5
# 2nd person reserves from for 3-8
# 3rd person reserver room from 6-10
# 4th person reserves room from 7-11
# 5th person reserves room from 15-18


# entry point to the app
def main():

    display_rooms()
    reserve_room("John", 1, 5)
    print("END of reservation 1")

    display_rooms()
    reserve_room("Mary", 3, 8)
    print("END of reservation 2")

    display_rooms()
    reserve_room("Sally", 6, 10)
    print("END of reservation 3")

    display_rooms()
    reserve_room("Bob", 7, 11)
    print("END of reservation 4")

    display_rooms()
    reserve_room("Jen", 15, 18)
    print("END of reservation 5")


if __name__ == '__main__':
    main()
