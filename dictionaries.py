products = {'vivo':5300, 'apple': 60000, 'xiaomi': 20000, 'oppo': 15000}

user_input = input(f"What item you want to buy {products} ") # asking the user
print(f"The Price of the item is {products[user_input]}") # output of the search item in the list showing what is the price
new_product = input("What Item you want to sell on us?") # asking the user what item they want to sell
new_price = input(f"How Much Do You Want To Sell The Item {new_product}?") # asking the price they want
products[new_product]=new_price # adding the user input to the list
print(f"The new product list is {products}") # printing the new list

price_updated = input("What product you want to update") # asking the user what item they want to update
price_change = input("What is  the price of item you want to change") # asking the price they want to update
products[price_updated]=price_change # using user input we are going to change the price of the selected item
print(f"The newly updated list is {products}") # printing the updated list
print(len(products))
keys = list(products.keys()) # slicing the  list in dictionaries
print(keys[0:3])
