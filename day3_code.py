print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height>=120:
    print("You can Ride")
else:
    print("Sorry still need to grow")


#to check the given number is odd or not    
    
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number%2==0:
    print("the given no is even")
else:
        print("the given no is odd")


        # 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=int(weight/(height*height))
print(bmi)
if bmi<=18.5:
    print("underweight")
elif bmi<=25:
    print("normal weight")
elif bmi<=30:
    print("slightly overweight")
elif bmi<=35:
    print("obese")
else:
    print("clinically obese.")


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")

    else:
        print("leap year")

else:
    print("not a leap year")



# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇S
A=0
B=0
C=0
cost_of_small=15
cost_of_midium=20
cost_of_large=25
if size=="S" :
    A=A+cost_of_small
elif size=="M":
    B=B+cost_of_midium
elif size=="L":
    C=C+cost_of_large
else:
    print("invalid entry")
if (add_pepperoni=='Y'and extra_cheese=='N'):
    if size=="S":
        A=A+2
        print("the total cost would be",A)
    elif (size=="M" and extra_cheese=='N') :
        B=B+3
        print("the total cost would be",B)
    elif (size=="L"and extra_cheese=='N' ):
        C=C+3
        print("the total cost would be",C)

            
if (add_pepperoni=='N'and extra_cheese=='N'):
    if size=="S":
        
        print("the total cost would be",A)
    elif (size=="M"and extra_cheese=='N') :
        
        print("the total cost would be",B)
    elif (size=="L"or extra_cheese=='N' ):
        
        print("the total cost would be",C)


if(add_pepperoni=="Y" and extra_cheese=='Y'):
    if size=="S":
        A=A+1
        A=A+2
        print("the total cost would be",A)
    elif size=="M":
        B=B+3    
        B=B+1
        print("the total cost would be",B)
    elif size=="L":
        C=C+1
        C=C+3
        print("the total cost would be",C)



# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combi=name1+name2
lower_case_string=combi.lower()


t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
true=t+r+u+e
print(f"total part A {true}")
love=l+o+v+e
print(f"total part B {love}")
love_score=print("love score= ",str(true)+str(love))
love_score=int(str(true)+str(love))


if (love_score<10) or (love_score>90):
    print(f"your score is {love_score}, you go together like coke and mentos.")
elif (love_score>=40 ) and (love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print("your score is",love_score)





