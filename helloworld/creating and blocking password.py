sys_password="1234"
user_password=""
no_of_try=0
no_of_max_try=9
max_try="not reached"

while user_password!=sys_password and max_try!="reached":
    if no_of_try<no_of_max_try:
        user_password=input("enter your password:")
        no_of_try=no_of_try+1
    else:
        max_try="reached"

if max_try=="reached":
    print("Account blocked")
else:
    print("Access granted..")