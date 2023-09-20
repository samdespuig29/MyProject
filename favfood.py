favoritefood: list[str] = ["burger", "fries", "fried chicken", "sundae", " spaghetti"]
print(favoritefood)
print(favoritefood[2])
favoritefood.append("milktea")# to be added to the last part of the list
print(favoritefood)
favoritefood.insert(2,"tacos") # insert in any index part of the list
print(favoritefood)
favoritefood[1]='italian food' # insert a item in specific index
print(favoritefood)

favoritefood[0:8]='cake', 'apple', 'banana', 'watermelon', 'orange', 'berry', 'blueberry' # mutability
print(favoritefood)

people = ("hotdog", "vegetable", "meat") # tuple permanent not editable
print(people)
thistuple = ("apple",)
print(type(thistuple)) # identify the class

fruits = ('banana', 'dragonfruit', 'apple' ) #tuple
print(fruits[-3]) #slicing tuple
people = {
    "anna":14,
    "sam":24,
    "luis":22
} #dictionaries
print(people["luis"])
people["samsam"] = 25 # adding item in list
print(people)
people_id = {1:"sam", 2:"luis", 3:"aruel"} # dictionaries
print(people_id[3]) # slicing in dict
del people_id[1] # deleted item in dict list
print(people_id)
people = dict(
    sam=24,
    luis=22,
    tim=21
) # dict method
people["mike"]=20 # adding item in dict method list
del people ["tim"] # deleting item in list
print(people)
print(people.get("luis")) # get method
price = {
    "cake":220,
    "juice":20,
    "fries": 35
}
new_price = {
    "cake":250,
    "juice":30,
    "fries":40
}
price.update(new_price) # using update method
print(price)
price = {
    "cake":220,
    "juice":20,
    "fries": 35
}
a = price.pop("juice") # using pop to see the item price
print(a)
price.pop("cake") # using pop removing item in list
print(price)
priceDiscount = {
    "cake":220,
    "juice":20,
    "fries": 35
}
print(priceDiscount.values()) # using dict values to print the price
print(priceDiscount.keys()) # using keys to print the items
print(priceDiscount.items()) # using items method to print the list
number = set([1,2,3,4,5,6]) # creating list using set method
print(number)
number = set() # creating a empty set
print(type(number))
