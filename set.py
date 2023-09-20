number = set([1,2,3,4,5,6]) # creating a set
print(number)
names = set() # creating empty set
print(type(names))
names = set(['sam',12,12.5,True])
print(names)

a = {'john','sam','tim'}
print("tim" == a)

setA = {1,2,3,4,5}
setB = {6,7,8,9,4}
print(setA | setB) # union operator

setA = {1,2,3,4,5}
SetB = {6,7, 8,9,0,5}
print(setA & setB) # comparing
print(setA - setB) # removing item using minus
print(setA ^ setB) # se metric  difference
setA = {1,2,3,4,5}
setA.add(10) # using add method
setA.remove(10) # using remove method
setA.discard(20) # safest way removing item in list without crashing
setA.pop() # removing randon item in list
a = setA.pop() # printing the item has been removed
print(a)
print(setA)
setA.clear() # clearing your set
print(setA)
