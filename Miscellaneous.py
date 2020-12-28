st = 'Create a list of the first letters of every word in this string'
l = st.split(" ")
for i in range(len(l)):
    print(l[i][0],end=" ")

List = [word[0] for word in st.split()]
print (List)


# FUNCTIONS in PYTHON
def check_even(list1):
    l = []
    for num in list1:
        if num % 2 == 0:
            l.append(num)
        else:
            pass
    return l
 
print(check_even([1,2,3,4,5,6,7,8,9,10]))


