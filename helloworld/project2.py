person_name1=input("enter the name of person 1")
person_name2=input("enter the name of person 2")
person_name3=input("enter the name of person 3")

slice_in_piza=input("enter the slice in the piza:")
prize_of_piza=input("enter the price of piza:")

percentage_age_by_person1=input("enter percentage ate by "+person_name1+ ": ")
percentage_age_by_person2=input("enter percentage ate by "+person_name2+ ":")
percentage_age_by_person3=input("enter percentage ate by "+person_name3+ ":")

v_percentage_age_by_person1=float(percentage_age_by_person1)/100
v_percentage_age_by_person2=float(percentage_age_by_person2)/100
v_percentage_age_by_person3=float(percentage_age_by_person3)/100

slice_ate_by_person1=float(v_percentage_age_by_person1)*float(slice_in_piza)
slice_ate_by_person2=float(v_percentage_age_by_person2)*float(slice_in_piza)
slice_ate_by_person3=float(v_percentage_age_by_person3)*float(slice_in_piza)

person1_bill=float(percentage_age_by_person1)*float(prize_of_piza)
person2_bill=float(percentage_age_by_person2)*float(prize_of_piza)
person3_bill=float(percentage_age_by_person3)*float(prize_of_piza)

print(person_name1+" ate "+str(slice_ate_by_person1)+ "slice and need to pay "+str(person1_bill)+ " inr")
print(person_name2+" ate "+str(slice_ate_by_person2)+ "slice and need to pay "+str(person2_bill)+ " inr")
print(person_name3+" ate "+str(slice_ate_by_person3)+ "slice and need to pay "+str(person3_bill)+ " inr")