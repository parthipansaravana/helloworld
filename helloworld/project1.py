# from math import *

rice=input("enter the quantity of the rice:\n")
dhal=input("enter the quantity of the dhall:\n")
bag=input("enter the quantity of the bag:\n")

rice_price=input("enter the price of the rice:\n")
dhal_price=input("enter the price of the dhal:\n")
bag_price=input(" enter the price of the bag:\n")

bill=(float(rice)*float(rice_price))+(float(dhal)*float(dhal_price))+(float(bag)*float(bag_price))
print("total bill ="+str(bill))