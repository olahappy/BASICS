#y/m/d format
# A module named datetime is used to work with dat as date objects
# From date time, we get the date and time
#Thats why I am impoerting date from datetime
from datetime import date

#def is used to define a function in python like function in php
def persons_age(persons_dob):
    #gets today's date
    today = date.today()
    # (6,12) < (2,1) ..... the person has celebrated his birthday but if its greater, the person has not celebrated his birthday
    persons_age = today.year - persons_dob.year - ((today.month, today.day) < (persons_dob.month, persons_dob.day))
    return persons_age

age = persons_age(date(1997,2,1)) 
print(age)

retirement_age = 65
if retirement_age > age:
    print(retirement_age - age)
else:
    print("This person's age is more than the retirement age")


#getting input from users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!" +", you are " + age + " years old")

#Getting two numbers from a user and performing math operations
# number1 = input("Enter a number ")
# number2 = input("Enter another number ")
# result = float(number1) + float(number2)
# print(result)