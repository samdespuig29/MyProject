products = ['shampoo', 'sardines','apple','banana']
 # item = input("Enter product to search ") # user input
 # print(item in products)  # comparing user  input in list

for product in products: # looping the whole list
    print(product.title()) # Capitalizing the item
DiscountedItem = ['phone', 'tablet', 'laptop', 'imac']
print(f"Current item in shop now on sale: {DiscountedItem}")

customerChoice = input("Enter product you want to buy: ")
DiscountedItem.remove(customerChoice)
print(f"Current item in shop now on sale: {DiscountedItem}")

add_item = input("What item you Want to return ")
add_after = input(f"After which product do you want place {add_item} ")
index = DiscountedItem.index(add_after)
DiscountedItem.insert(index+1,add_item)
# DiscountedItem.append(add_item)
print(f"Current item in shop now on sale: {DiscountedItem}")