List = ['apple', 'mango', 'pineapple', 'orange', 'grape', 'peach', 'watermelon']
print(List[2])  # positive indexing accessing array
print(List[-6])  # negative indexing
print(List[0:7])  # positive list slicing
print(List[-4:])  # negative list slicing
print('tomato' not   in List) # in not operator
print(len(List)) # length of list
List.insert(2, "cherry") # insert func
print(List)
List.append("star apple") # append to List
print(List)
List.append(["guava", "apricot"]) # added to list
List.extend(["berry", "pico"]) # added item in list
 # List.remove("apple") # removing item in list
 # List.pop() #  removing last item in list
print(List.index("mango"))
print(List)
scores = [23,453,232,323,2323]
print(min(scores))

sales = [12,21,23,[55,32,545,[366,88,9,67]],234,54,65,[43.45,756]]
print(sales[7][1])
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
