# print("hello"[2])
# print("123"+"345")
# print(123+345)

# # #type conversion error
# # a=len(input("what is your name?"))
# # print("your name has "+a+" characters")


# #type conversion error rectified
# a=len(input("what is your name?"))
# print("your name has "+str(a)+" characters")

# #type conversion
# a=str(123)
# print(type(a))

# print(70+float("100.5"))
# print(str(70)+str(100))

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# two_digit_number = input("Type a two digit number: ")
# print(two_digit_number)
# a=int(two_digit_number[0])
# b=int(two_digit_number[1])
# print(a+b)


# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# H=float(height)
# W=int(weight)
# BMI=W/(H**2)
# print(int(BMI))

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# years_left=(90-int(age))

# age_leftin_months=years_left*12

# age_leftin_days=years_left*365
# age_leftin_weeks=years_left*52
# print(f"You have {years_left} years left.,and{age_leftin_days}in days,{age_leftin_weeks}in weeks,{age_leftin_months}in months")

#welcome to the project of the tip calculator

print("welcome to the tip calculator")
total_bill=float(input ("pls enter the total bill "))
num_of_people=int(input("no of people to share the bill"))
tip=float(input("enter the how much percentage u will tip"))
bill_split=round((total_bill)/num_of_people,2)

tip_cal=(bill_split*float(tip))/100
each_person_pay=(bill_split+tip_cal)
print(round(each_person_pay,2))









