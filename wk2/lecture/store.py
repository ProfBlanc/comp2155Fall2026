"""
App will allow user to
add products to a cart
a product has a name and price
a cart has many products and quantities of product
user should be able to checkout
when checking out => bill is calculated
final price displayed with tax (13%)
functions, modules, controls construct

"""
# variable name is cart : data type is str = value is this
#cart:str = ""

# declaring the expected data type values
cart: list[dict[str, float]] = []


def add_product(name: str, price: float):
    if len(name) < 3 or price < 1:
        raise ValueError("Invalid product.")
    # limitation is that only 1 quantity of the product is added

    # iterate through the car
    # determine if exact name and price already exists
    # if so, increase quantity. if not, add item to cart
    item_found = False
    for item in cart:
        if item["name"] == name and item["price"] == price:
            item["quantity"] += 1
            item_found = True
            break

    if not item_found:
        cart.append({"name": name, "price": price, "quantity": 1})

    return name, price  # return as a tuple

def checkout():
    if len(cart) == 0:
        raise ValueError("Empty cart.")
    calculate_bill()

def calculate_bill():
    """
    iterate through cart to determine the final price
    """
    total_price = 0
    tax_price = 0
    grand_total_price = 0
    tax_rate = 0.13
    """
    for item in cart:
        total_price += item["price"] * item['quantity']
    """

    total_price += sum([item['price'] * item['quantity'] for item in cart])
    # for item in cart
    # item['price'] for item in cart

    tax_price = total_price * tax_rate
    grand_total_price = total_price + tax_price

    return total_price, tax_price, grand_total_price

def display_bill():
    # should add an exception if no items in cart
    if len(cart) == 0: raise ValueError("Empty cart")
    for item in cart:
        print("Item Name: ", item["name"])
        print("Item Price: ", item["price"])
        print("Item Quantity: ", item["quantity"])

    total, tax, grand_total = calculate_bill()

    print("Total Price", total)
    print("Tax", tax)
    print("Grand Total", grand_total)
