#Advanced Number

print(hex(246)) #convert number in hexadecimal format
print(bin(1234)) #convert number in binary format
print(pow(3,4))
print(abs(-3.14))
print(round(395,-2))
print(round(3.141592,2))

#Advanced String
print("\n ADVANCED STRING \n")
s = 'hello world'
print(s.capitalize())
print(s.count('o'))
print(s.find('o'))
print(s.center(20,'*'))

print(s.isalnum(),s.isalpha(),s.islower(),s.isupper(),s.isspace(),s.istitle(),s.isdigit())
print(s.endswith('o'))
print(s.startswith('h'))
print(s.split(" "))
print(s.partition('o'))

#Advanced Set
print("\n ADVANCED SET \n")
s = set()
s.add(1)
s.add(2)
print(s)
sc={1,2,3,4}.copy()
print(sc)
print(sc.difference(s)) #difference of two set
print(s.difference(sc))
print(sc.discard(2)) #remove an element
print(s.intersection(sc)) #intersection of two set
print(s.intersection_update(sc))
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s1.issubset(s2)) #check subset
print(s2.issuperset(s1)) #check superset
print(s1.symmetric_difference(s2)) #return symmetric difference of two set as a new set
print(s1.union(s2)) # Union
s2.update(s3) #update
print(s2)

#Advanced Dictionaries
print("\n ADVANCED DICTIONARIES \n")

d = {'k1':1, 'k2':2}
for k in d.keys():
    print(k,end=" ")
print("")
for v in d.values():
    print(v,end=" ")
print()
for items in d.items():
    print(items,end=" ")

#Avanced List
print("\n ADVANCED LISTS \n")

list1 = [1,2,3]
list1.append(4) #append()
print(list1)  
print(list1.count(2)) #count()
x = [1,2,3]
x.append([4,5]) #append(list)
print(x)
x = [1,2,3]
x.extend([4,5]) #extend(list)
print(x)
print(list1.index(2)) #index of element
list1.insert(2,'inserted')
print(list1)