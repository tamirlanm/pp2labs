#Boolean examples
#ex1
print(10 > 9)
print(10 == 9)
print(10 < 9)
#answer: True

#ex2
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#answer: b is not greater than a
  
#ex3
print(bool("Hello"))
print(bool(15))
#answer: True

#ex4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#answer: True

#ex5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#answer: True

#ex6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#answer: False

#ex7
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#answer: False

#ex8
def myFunction() :
  return True
print(myFunction())
#answer: True

#ex9
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#answer: YES!

#ex10
x = 200
print(isinstance(x, int))
#answer: True

#Operators examples
#ex1
print(10 + 5)
#answer: 15

#ex2
print((6 + 3) - (6 + 3))
#answer: 0

#ex3
print(100 + 5 * 3)
#answer: 115

#ex4
print(5 + 4 - 7 + 3)
#answer: 5

#Lists examples
"""ex1
Create a list:"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

#ex2
#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#ex3
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#ex4
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#ex5
#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#ex6
#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#answer: <class 'list'>

#ex7
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#acces list items
#ex1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#ex2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#ex3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#ex4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#ex5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#ex6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#ex7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change list items
#ex1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) 
#answer: ['apple', 'blackcurrant', 'cherry']

#ex2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#ex3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#ex4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#ex5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

#add list items
#ex1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#ex2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#ex3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ex4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove list items
#ex1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ex2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#ex3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#ex4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#ex5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#ex6
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

#ex7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop througha a list
#ex1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#ex2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#ex3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):  
  print(thislist[i])
  i = i + 1

#ex4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension
#ex1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#ex2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#ex3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#ex4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

#ex5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10)]
print(newlist)

#ex6
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10) if x < 5]
print(newlist)

#ex7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#ex8
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

#ex9
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sort lists
#ex1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#ex2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#ex3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#ex4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#ex5
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#ex6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#ex7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#ex8
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 

#copy lists
#ex1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#ex2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join lists
#ex1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#ex2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#ex3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#list methods
"""
append()	// Adds an element at the end of the list
clear()	// Removes all the elements from the list
copy()	// Returns a copy of the list
count()	// Returns the number of elements with the specified value
extend() // Add the elements of a list (or any iterable), to the end of the current list
index()	// Returns the index of the first element with the specified value
insert()	// Adds an element at the specified position
pop()	// Removes the element at the specified position
remove()	// Removes the item with the specified value
reverse()	// Reverses the order of the list
sort()	// Sorts the list
"""

#Tuple examples
#ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ex2
#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#ex3
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

#ex4
#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#ex5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#ex6
tuple1 = ("abc", 34, True, 40, "male")

#ex7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#answer:<class 'tuple'>

#ex8
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#access tuples
#ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#ex2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#ex3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,

#ex4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#ex5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#ex6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

#ex7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#answer: Yes, 'apple' is in the fruits tuple

#update tuples
#ex1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#ex2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#ex3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#ex4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#ex5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#unpack tuples
#ex1
fruits = ("apple", "banana", "cherry")
print(fruits)

#ex2
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#ex3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#ex4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#loop tuples
#ex1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#ex2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#ex3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join tuples
#ex1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#ex2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#tuple methods
"""
count()  //  Returns the number of times a specified value occurs in a tuple
index()	 //  Searches the tuple for a specified value and returns the position of where it was found
"""

#Sets
#ex1
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

#ex2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#ex3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#ex4
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#ex5
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#ex6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#ex7
set1 = {"abc", 34, True, 40, "male"}
print(set1)

#ex8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#answer: <class 'set'>

#ex9
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.

#access set items
#ex1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#ex2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#answer: True

#add set items
#ex1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#ex2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#ex3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove set items
#ex1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#ex2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#ex3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

#ex4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#ex5
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists

#loop sets
#ex1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join sets
#ex1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#ex2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#ex3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#ex4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#ex5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#ex6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#ex7
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

#set methods
"""
add()	 //  Adds an element to the set
clear()  //  Removes all the elements from the set
copy()  //  Returns a copy of the set
difference()	 //  Returns a set containing the difference between two or more sets
difference_update()  // 	Removes the items in this set that are also included in another, specified set
discard()	 //  Remove the specified item
intersection()	 //  Returns a set, that is the intersection of two other sets
intersection_update()	  //  Removes the items in this set that are not present in other, specified set(s)
isdisjoint()  //  Returns whether two sets have a intersection or not
issubset()	 //  Returns whether another set contains this set or not
issuperset()  //  Returns whether this set contains another set or not
pop()	 //  Removes an element from the set
remove()	 //  Removes the specified element
symmetric_difference()	 //  Returns a set with the symmetric differences of two sets
symmetric_difference_update()	  //  inserts the symmetric differences from this set and another
union()	 //  Return a set containing the union of sets
update()	 //  Update the set with the union of this set and others
"""

#Dictionaries
#ex1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#ex2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#ex3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#ex4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

#ex5
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#ex6
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#answer : <class 'dict'>

#ex7
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 

#access dictionary items
#ex1 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#ex2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

#ex3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)

#ex4
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#ex5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

#ex6
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#ex7
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#ex8
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)

#ex9
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#ex10
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#ex11
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#change dictionaries items   
#ex1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#ex2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#add dictionaries items
#ex1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#ex2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

#remove dictionary items
#ex1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#ex2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#ex3
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#ex4
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#ex5
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#loop dictionaries
#ex1
for x in thisdict:
  print(x)

#ex2
for x in thisdict:
  print(thisdict[x])

#ex3
for x in thisdict.values():
  print(x)

#ex4
for x in thisdict.keys():
  print(x)

#ex5
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#copy dictionaries
#ex1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#ex2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#nested dictionaries
#ex1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#ex2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#ex3
print(myfamily["child2"]["name"])

#dictionary methods
""""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

#If ... else
#ex1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ex2
a = 33
b = 200
#if b > a:
#print("b is greater than a") # you will get an error

#ex3
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#ex4
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#ex5
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

#ex6
if a > b: print("a is greater than b")

#ex7
a = 2
b = 330
print("A") if a > b else print("B")

#ex8
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#ex9
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#ex10
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#ex11
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#ex12
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#ex13
a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement

#While loops
#ex1
i = 1
while i < 6:
  print(i)
  i += 1

#ex2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#For loops
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ex2
for x in "banana":
  print(x)

#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex6
for x in range(6):
  print(x)

#Ex7
for x in range(2, 6):
  print(x)

#ex8
for x in range(2, 30, 3):
  print(x)

#ex9
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#ex10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#ex11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#ex12
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement