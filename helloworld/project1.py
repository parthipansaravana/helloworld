from math import *

rice=input("enter the quantity of the rice:")
dhal=input("\nenter the quantity of the dhall:")
bag=input("\nenter the quantity of the bag:")

rice_price=input("\n enter the price of the rice:")
dhal_price=input("\n enter the price of the dhal:")
bag_price=input("\n enter the price of the bag:")

bill=(float(rice)*float(rice_price))+(float(dhal)*float(dhal_price))+(float(bag)*float(bag_price))
print("\ntotal bill ="+str(bill))