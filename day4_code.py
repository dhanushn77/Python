#randomise the num i.e int
import random
random_int=random.randint(1,30)
print(random_int)
#---------------------------------------------------------------------------------------

#randomise the num i.e float 
import random
random_float=random.random()*5
print(random_float)
#--------------------------------------------------------------------------------------------

import random
love_score=random.randint(1,100)
print(f"your love score would be {love_score}")
#--------------------------------------------------------------------------------------------

import random
love_score=random.randint(1,6)
print(f"dice number would be {love_score}")
#--------------------------------------------------------------------------------------------
import random
H_or_T=random.randint(0,1)

if (H_or_T==1):
    print("Heads")
else:
    print("Tails")
-#---------------------------------------------------------------------------------------------
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
states_of_america[1]="dellware"#it is used to correct or change in the specific position
print(states_of_america)
states_of_america.append("dhanush")#used to add the extra item
print(states_of_america)
states_of_america.extend(["hello","good"])
print(states_of_america)
#----------------------------------------------------------------------------------------


https://www.askpython.com/python/string/convert-string-to-list-in-python
 #to convert string to lists

#-------------------------------------------------------------------------------------------
# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line
a=len(names)
Radm=random.randint(0,a-1)
T=names[Radm]
print(f"{T}is going to pay the bill")
#--------------------------------------------------------------------------------------------

https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
#to generate random numbers

#-----------------------------------------------------------------------------------------------
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])#The first  index represent 'vegetables' i.e 1 and 'fruit' i.e 0 and second index represent inside vegitable index here
print(dirty_dozen[1][2])#Tomatoes
print(dirty_dozen[1][3])#Celery
print(dirty_dozen[0][3])#grapes

#---------------------------------------------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal=int(position[0])
vertical=int(position[1])
selected_row=map[vertical-1]
selected_row[horizontal-1]="X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")









