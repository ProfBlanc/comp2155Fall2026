"""
a theatre has a LIST of movies
a movie has a title and min age requirement

a person orders tickets to a movie
a ticket has title and showing time and num tix

a person pays for the ticket
    tax, subtotal, grand total
"""

# values
movies:list[dict[str,int]] = list()
tickets = list()


# a dictionary is a key-value pair
# each value stores has a key and a value
# invoice/bill: item_name   and quantity



# functions

def add_movie(title: str, min_age: int):
    if len(title) < 3 or min_age < 5:
        raise ValueError("Invalid movie")
    # disallow duplicate movie values
    for movie in movies:
        if movie['title'].lower() == title.lower():
            raise ValueError("Movie already exists")

    movies.append({"title": title, "min_age": min_age})

# add in a way to validate if person is of age to view movie
def buy_tickets(title: str, price: float, show_time: str, num_tickets: int):
    tickets.append({"title": title,
                    "price": price,
                    "show_time": show_time,
                    "num_tickets": num_tickets})

def calculate_bill():
    if len(tickets) == 0: raise ValueError("No tickets")
    sub_total = sum([ tix['num_tickets'] * tix['price']  for tix in tickets ])
    tax = sub_total * 0.13
    grand_total = sub_total + tax
    return sub_total, tax, grand_total

def display_bill():
    if len(tickets) == 0: raise ValueError("No tickets")
    sub_total, tax, grand_total = calculate_bill()
    for tix in tickets:
        print("Title", tix['title'])
        print("Price", tix['price'])
        print("Num Tickets", tix['num_tickets'])
        print("*" * 10)
    print("Sub Total", sub_total)
    print("Tax", tax)
    print("Grand Total", grand_total)