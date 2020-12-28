''' Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is unordered, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values '''

#Create and print a dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

#Print the "brand" value of the dictionary
print(thisdict["brand"])

#Dictionaries cannot have two items with the same key/ Duplicate values will overwrite existing values:
thisdict1 = {"brand": "Ford",  "model": "Mustang",  "year": 1964, "year": 2020}
print(thisdict1)

#Dictionary Length
print(len(thisdict))

#Accessing Items
#There is also a method called get() that will give you the same result: Get the value of the "model" key:
x = thisdict.get("model")

#Get a list of the keys:
x = thisdict.keys()

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get a list of the values:
x = thisdict.values()

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Get a list of the key:value pairs
x = thisdict.items()
print(x)

#Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values
thisdict["year"] = 2018
print(thisdict)

#Update the "year" of the car by using the update() method
thisdict.update({"year": 2020})
print(thisdict)

#ADD ITEMS
#Add a color item to the dictionary by using the update() method:
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.update({"color": "red"})
print(thisdict2)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict3["color"] = "red"
print(thisdict3)

#The del keyword can also delete the dictionary completely
'''del thisdict3
print(thisdict3) # Cause error'''

#The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

#Loop Through a Dictionary
#Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

for x in thisdict.keys():
    print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
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
print(myfamily)
