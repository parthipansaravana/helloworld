# with math function we can use numerical function from math
from math import *

#we can use all types of number like complete number(40)
#negative number(-40),float number(40.5),ect

print(10+10)

# priority operation will be taken first * is more priority then +
print(10+10*3)

# bracket has more preority then *
print((10+10)*3)

# when multiple arithmetic operation take place you need to use proper parathiences
print((((10+10)/4)*4)-40)

# if number inside a "" is taker as string we cant's perform any math operation
print("100",20)


# to perform a operation with a string value we need to store numer value in a varable and use variable in print
age=20
age=age+5
print("my age is "+str(age))

# without str funcion
B="30"
print("my age is "+B)

#max function
print(max(1,3,-5,3,5))

#min function
print(min(1,-55,33,4))

# calculate power
print(pow(5,2))
print(52/32+pow(5,2))

#round function
print(round(52/36+pow(5,2)))
print(-round(52/36+pow(5,2)))

# absolute value
print(abs(-round(52/36+pow(5,2))))

# square root
print(sqrt(16))

# ceil function round the value in a float
print(ceil(39.555))
print(ceil(-7.3))

# factorial function
print(factorial(3))
print(factorial(100))