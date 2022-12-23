person1_name=input("enter person 1 name:")
person1_height=input("enter person1 height:")
person2_name=input("enter person2 name:")
person2_height=input("enter person2 height:")
person3_name=input("enter person3 name:")
person3_height=input("enter person3 height:")

if float(person1_height)>float(person2_height) and float(person1_height)>float(person3_height):
    print(person1_name+" is heights person among three.")
elif float(person2_height)>float(person1_height) and float(person2_height)>float(person3_height):
    print(person2_name+" is heightest among three.")
else:
    print(person3_name+" is heightst among three.")