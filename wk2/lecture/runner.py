import store
from store import *

# result = store.add_product(name="Food", price=20)
# # result = store.add_product(name="Fo", price=.20)
#
# product_name = input("Enter product name: ")
# product_price = float(input("Enter product price: "))
#
# result = add_product(name=product_name, price=product_price)
# print(result)

add_product("Pizza", 16)
add_product("Pizza", 15)
add_product("Pizza", 15)
add_product("Wings", 20)

# dictionary SHOULD be [{name: Pizza, price: 15, quantity: 2}, ...]
# dictionary ACTUALLY [{name: Pizza, price: 15, quantity: 1},
# {name: Pizza, price: 15, quantity: 1}]

display_bill()