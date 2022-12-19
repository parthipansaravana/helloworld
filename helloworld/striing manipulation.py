sentence="heLlo"
print(sentence)

# to convert string into upper case
print(sentence.upper())

# to convert string into lower case
print(sentence.lower())

# to check the sentence is upper case or not
print(sentence.isupper())

# to check the sentence is lower case or not
print(sentence.islower())

# to convert the string and check the string is lower or not
print(sentence.lower().islower())

# to convert the string into lower case and save in A
A=sentence.lower()
print(A)

# to convert upper case and store in B
B=sentence.upper()
print(B)

# to check A is a lower case or not
print(A.islower())

# to check A is upper or not
print(A.isupper())


# to check B is lower case or not
print(B.islower())

# to check B is upper case or not
print(B.isupper())

# to calculate string size
print(len(sentence))

# to save string in c and replACE  C by hi
c=sentence
print(c.lower().replace("hello","hi"))

# to check the index value of the string element
print(c.index("e"))

# to change the sentence into lower case and check index of l in sentence
print(sentence.lower().index("l"))


#in multi word string if we find the index of the word the out will be the index of 1st letter
D="hello world"
print(D.index("world"))

# to print a single string in multiple line
print("i am\n parthipan")