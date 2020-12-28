#A tuple is a collection which is ordered and unchangeable(order of element cannot be changed).
#Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[-1])
print(thistuple[2:4])

#length of tuple
print(len(thistuple))

#A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Convert the tuple into a list to be able to change it bcoz tuple is unchangable
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Unpacking a tuple using *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#Search for the first occurrence of the value 8, and return its position
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)


#Unpacking of Tuples
stock_prices = [('Apple', 200), ('Google', 400), ('Microsoft',100)]
for item, price in stock_prices:
    print(item)
    print(price)


work_hours = [('Abby', 100), ('Billy', 400), ('Cassie',800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)

print (employee_check(work_hours))
