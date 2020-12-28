#Get the characters from position 2 to position 5
b = "Hello, World!"
print(b[2:5])

#Get the characters from the start to position 5 and position 2 to end 
print(b[:5])
print(b[2:])

#Use negative indexes to start the slice from the end of the string
print(b[-5:-2])

#Jump in string
print(b[::2])

# STRING IN-BUILD METHODS #

#Upper case & Lower Case of String
print(b.upper())
print(b.lower()) 

#The strip() method removes any whitespace from the beginning or the end
print(b.strip())

#The replace() method replaces a string with another string
print(b.replace("H", "J"))

#The split() method returns a list where the text between the specified separator becomes the list items
print(b.split(","))

#find the starting position of string
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#Return the number of times the value "apple" appears in the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

#Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
x = txt.index("e", 5, 10)
print(x)

#Check if all the characters in the text are alphanumeric/alphabet/digit:
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "123456"
x = txt.isdigit()
print(x)

#Join all items in a tuple/Dictionary into a string, using a hash character as separator
myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

