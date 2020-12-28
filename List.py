#List allow duplicate elements

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[2][3])
print(thislist[2:4])


#length of list
print(len(thislist))

#List items can be of any data type
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#To determine if a specified item is present in a list use the in keyword
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#To change the value of a specific item, refer to the index number
thislist[1] = "blackcurrant"
print(thislist)

#Change the second value by replacing it with two new values
thislist[1:2] = ["banana", "watermelon"]
print(thislist)

#The insert() method inserts an item at the specified index
thislist.insert(2, "Guavaa")
print(thislist)

#Using the append() method to append an item
thislist.append("orange")
print(thislist)

#Remove specified items
thislist.remove("banana")
print(thislist)

thislist.pop(1)
print(thislist)             #remove element using Index

#for using in form of loop
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list = []
for x in fruits:
  if "a" in x:
    list.append(x)
print(list)

#Sort the List alphabetically
thislist.sort()
print(thislist)

#Sort list in descending order
thislist.sort(reverse = True)
print(thislist)

#Copy a List
mylist = thislist.copy()
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)
print(list1)

list1.extend(list2)
print(list1)

#Removes all the elements from the list
list1.clear()
print(list1)