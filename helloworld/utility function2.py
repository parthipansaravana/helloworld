def rec(name):
    print(name+",how can i help you.")
def res(name,food,table,beverage):
    name=input("may i know your name:")
    food=input("What did you like to eat:")
    table=input("May i know your table number:")
    beverage=input("Did u need any beverage after food:")
    print(str(name)+" you ordered "+str(food)+ " beverage is " +str(beverage)+" any your table is "+str(table))

def tnk(name):
    print(name+" thank you")
rec("Reception")
res("name","food","table","beveraage")
tnk("reception")