item  = ['notebook', 'pencil', 'ballpen', 'eraser']

item_remove = input(f"What item you want to buy {item} ") #  asking the user to input the item want to buy also displaying list
item.remove(item_remove) # Remove function
print(f"All  the item available in the list is {item}") # Displaying the available list
add_item = input("What Item you Want to sell on us?")
add_to_the_list = input("What place  do you  Want to place the item you sell ")

index = item.index(add_to_the_list) # creating the index in the list
item.insert(index+1,add_item) # function for inserting the item in the list
print(f"All  the item available in the list is {item}") # Displaying the available list


