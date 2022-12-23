def calculate():
    a=input("do you like to answer every question by your own by yes or no only:")
    if a!="yes":
        print("try again  yes/no:")
    else:
        print("lets start")
        q1=input("are you hungry yes/no: ")
        if q1!="yes":
            return print("ok lets eat later.")
        else:print("next question")
        q2=input("do you like idly?")
        if q2!="yes":
            return print("ok we will go to restraunt.")
        else:print("next question")
        q3=input("do you need more idly?")
        if q3!="yes":
            return print("drink the milk after complete idly")
        else:
            return print("thank you for ask more idly but unfortunaly idlys are over.")
calculate()