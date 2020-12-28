print("String Tutorial")
a = "Hrishabh Singh"
print(a)
print(a[2])
print(a[-5])
print(len(a))

for x in "Harry":               #Loop through the letters in the word
    print(x)
for x in "Harry":               #Loop through the letters in the word and print in same line
    print(x, end=" ")
print("\n")

#Check if "free" is present in the following text
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

