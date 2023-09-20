order = []
total_price = 0.0

menu = {
    1: {"description": "Jolly Spaghetti with Drink", "price": 5.99},
    2: {"description": "Jolly Spaghetti with 1pc Jolly Crispy chicken & Drink", "price": 7.99},
    3: {"description": "Jolly Spaghetti Family pack", "price": 14.99},
    4: {"description": "Jolly Crispy Chicken 2pc w/ 1 side & Drink", "price": 7.49},
    5: {"description": "Jolly Crispy Chicken 2pc w/ 2 sides & Drink", "price": 8.49},
    6: {"description": "Jolly Crispy Chicken 3pc w/ 1 side & Drink", "price": 9.49},
    7: {"description": "Jolly Crispy Chicken 3pc w/ 2 sides & Drink", "price": 10.49},
    8: {"description": "6pc Jolly Crispy Chicken Bucket", "price": 13.99},
    9: {"description": "Bucket treat (1 Jolly Crispy Chicken Bucket, 3pcs Mashed Potatoes, 3pcs Peach Mango Pies)",
        "price": 26.49},
    10: {
        "description": "Bucket treat (1 Jolly Crispy Chicken Bucket, 1pc Spaghetti Family Pack, 3pcs Peach Mango Pies)",
        "price": 32.99},
    11: {"description": "Bucket treat (2 Jolly Crispy Chicken Buckets, 6 Steamed Rice, 6 Chocolate Sundaes)",
         "price": 45.49},
    12: {"description": "Peach Mango Pies", "price": 2.49},
    13: {"description": "Chocolate Sundae", "price": 2.29},
    14: {"description": "Vanilla Twirl", "price": 1.39},
    15: {"description": "1pc Jolly Crispy Chicken w/ Rice & Drink", "price": 4.99},
    16: {"description": "Jolly Spaghetti w/ Drink", "price": 4.99},
    17: {"description": "Yum w/ cheese, Small fries & Drink", "price": 4.99},
    18: {"description": "Steamed Rice", "price": 1.25},
    19: {"description": "Mashed Potato (Large)", "price": 3.49},
    20: {"description": "Mashed Potato (Regular)", "price": 2.49},
    21: {"description": "Buttered Corn (Large)", "price": 3.49},
    22: {"description": "Buttered Corn (Regular)", "price": 2.49},
    23: {"description": "French Fries (Large)", "price": 3.49},
    24: {"description": "French Fries (Regular)", "price": 2.49},
    25: {"description": "Yum w/ Cheese w/ fries & Drink", "price": 3.99},
    26: {"description": "Yum w/ Cheese (Regular)", "price": 1.99},
    27: {"description": "Big Yum w/ fries & Drink", "price": 7.99},
    28: {"description": "Big Yum (Regular)", "price": 5.99},
    29: {"description": "Aloha Yum w/ fries & Drink", "price": 8.49},
    30: {"description": "Aloha Yum (Regular)", "price": 6.49},
    31: {"description": "2pcs Burger steak w/ Drink 1 Side", "price": 6.49},
    32: {"description": "2pcs Burger steak w/ Drink 2 Sides", "price": 7.49},
    33: {"description": "Palabok Fiesta w/ Drink", "price": 6.99},
    34: {"description": "Palabok Fiesta w/ 1pc Jolly Crispy Chicken & Drink", "price": 8.99}
}

print("\n=====================================================")
print("=======================WELCOME=======================")
print("=====================JOLLIBEE INC.===================")
print("=====================================================")

print("Here is the menu:")
for item, details in menu.items():
    print(f"[{item}] - {details['description']} - ${details['price']:.2f}")

print("How many Orders?")
n = int(input())

print("\n")
print("=====================================================")
print("=================CUSTOMER ORDERS====================")
print("=====================================================")

for i in range(n):
    print(f"Order {i + 1}:")
    choice = int(input("Enter your choice: "))

    # Ask for the number of servings for the selected item
    servings = int(input(f"How many servings of {menu[choice]['description']} would you like to order? "))

    order.append((choice, servings))

print("\n=====================================================")
print("==============CUSTOMER ORDER SUMMARY================")
print("=====================================================")

for i, (item, servings) in enumerate(order):
    item_description = menu[item]['description']
    item_price = menu[item]['price']
    if servings > 0:
        print(
            f"Order {i + 1}: [{item}] - {item_description} - ${item_price:.2f} x {servings} = ${item_price * servings:.2f}")
        total_price += item_price * servings
    else:
        print(f"Order {i + 1}: [{item}] - {item_description} - $0.00 (No servings)")

print("\nTotal Price: ${:.2f}".format(total_price))
print("\n=====================================================")
print("====================== RECEIPT =====================")
print("=====================================================")

total_price = 0.0

for i, (item, servings) in enumerate(order):
    item_description = menu[item]['description']
    item_price = menu[item]['price']
    subtotal = item_price * servings
    total_price += subtotal

    print(f"Order {i + 1}: [{item}] - {item_description}")
    print(f"   Price per serving: ${item_price:.2f}")
    print(f"   Servings: {servings}")
    print(f"   Subtotal: ${subtotal:.2f}")
    print("-----------------------------------------------------")

print(f"Total Price: ${total_price:.2f}")
print("=====================================================")