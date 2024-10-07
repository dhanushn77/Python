# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height=0
for height in student_heights:
    total_height=total_height+height
print(total_height)

num_of_students=0
for length in student_heights:
    num_of_students+=1
print(num_of_students)
print(round(total_height/num_of_students))
#--------------------------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# 🚨 Don't change the code above 👆

#Write your code below this row 👇
heigst_scores=0
for scores in student_scores:
    if scores>heigst_scores:
        heigst_score=scores
print(f"the heighst score is {heigst_score}")
#-----------------------------------------------------------------------------------------------------
 #You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
add=0
for number in range(2,101,2):
    add=add+number
print(add)
  # or
   
# #alternative_sum = 0
# for number in range(1, 101):
#   if number % 2 == 0:
#     # print(number)
#     alternative_sum += number
# print(alternative_sum)
#---------------------------------------------------------------------------------------------------
 
#   Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#  `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for number in range(1,101):
    
    if (number%3==0 and number%5==0):
            print("FizzBuzz")
    
    elif (number%3==0):
        print("Fizz")
    elif (number%5==0):
            print("Buzz")
    
    else:
        print(number)
#---------------------------------------------------------------------------------------------------------------
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

    #--------------------------------------------------------------------------------------------------
   
    