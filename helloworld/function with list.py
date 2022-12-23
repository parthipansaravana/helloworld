# list instialization
a=[5,4,3,7,8,3,7,8]
b=["apple","banana","cherry","dragon","eliche","cherry","dragon","eliche"]

# print list before insert
print(a)
print(b)

# COPYFUNCTION
# to copy the list element into a variable and use
c=a.copy()
print(c)
# copy multiple list into one variable
d=a.copy()+b.copy()
print(d)


# INSERT FUNCTION
# insert values into list
a.insert(3,6)
b.insert(2,"pinapple")

# print after insert
print(a)
print(b)

# EXTEND FUNCTIOM
# integrate or join two list
a.extend(b)

# print after integration of a
print(a)
print(b)



# INDEX FUNCTION
# to find the index of the element in the list
print(a.index(5))
print(b.index("cherry"))

# COUNT FUNCTION
# to count the number of occurance
print(a.count(8))
print(b.count("cherry"))

# CLEAR FUNCTION
# clear the list value
a.clear()
b.clear()

# print list after clear
print(a)
print(b)