# name = input("What is your name????"'\n')
# color = input("What is your favourite color????"'\n')
# print(name +" likes "+ color)
import json

# birth_year = input('Birth year : ')
# age = 2019 - int(birth_year)
# print(age)

# Weight_Kilogram = input("Please enter your weight in kilogram:")
# Weight_Pound = int(Weight_Kilogram) * 1.75
# print(Weight_Pound)

# Title = "This is python tutorial"
# Sub_Title = Title
# print(Sub_Title[1])
# print(Title[2])
# print(Title[-1])
# print(Title[0:8])
# print(Title[0:])
# print(Title[1:])
# print(Title[:9])
# print(Title[1:-1])

# First = "Vinay"
# Last = "Sagare"
# Message = f'{First} {Last} is a Coder'
# print(Message)

# Len Function
# Course = 'Python is programming language'
# print(len(Course))
# print(Course.upper())
# Course = 'VINAY SAGARE'
# print(Course.lower())
# Ans = len(Course) * 30
# print(Ans)
# print(Course.find('G'))
# print(Course.find('g'))

# in Function
# print('VINAY' in Course)
# print(Course.title())
# print(Course.replace('VINAY','MEGHA'))

# Arithmatic Operation
# print(10**3)

# Math Function
# x = 2.3
# y = 2.9
# z = -2.22
# print(round(x))
# print(round(y))
# print(abs(z))

# import math
# x = 2.3
# print(math.ceil(x))
# print(math.floor(x))

# Statements in Python
# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("Its hot day")
# elif is_cold:
#     print("Its cold day")
# else:
#     print("Its Lovely Day")

# good_credit = False
# house_price = 1000000
# if good_credit:
#     House_Price = (house_price*10)/100
# else:
#     House_Price = (house_price*20)/100
# print(f"Your House rent is : {House_Price}")

# AND Operator
# good_credit = True
# good_personality = True
# has_Criminal_Record = True
# if good_credit and good_personality and not has_Criminal_Record:
#     print("Man is Perect")
# else:
#     print("Man is not Perfect")

# Comparator Operator
# good_credit = 1000000
# if good_credit >100000 :
#     print("Man is Perect")
# else:
#     print("Man is not Perfect")

#  Weight Converter
# Weight = int(input("Enter your Weight"))
# Unit = input('(L)bs or(K)g :')
# if Unit.upper() == "L":
#     Converted = Weight*45
#     print(f"you are {Converted} kilos")
# else:
#     Converted = Weight / 0.45
#     print(f"you are {Converted} pounds")

# While Loop
# Number = 9
# i = 0
# while 3 > i:
#     Input = int(input("Enter Guess number: "))
#     i +=1
#     if Input == Number:
#         print("You Win")
#         break
# else:
#     print("Sorry, You failed")

# For Loops
# for item in 'PYTHON':
#     print(item)
#
# for item in ['Vinay','Sagare']:
#     print(item)
#
# for item in range(1,10,):
#     print(item)
#
# for item in range(1,10,3):
#     print(item)

# NestedLoops
# for x in range(4):
#     for y in range(3):
#         print(f'({x} ,{y})')

# Number = [5,2,5,2,2]
# for x in Number:
#     print('x' * x)

# Number_List = [1,2,3,5,65,34,78,98,23,45,7,6,76,89,91,95,33]
# gretest_number = 0
# for x in Number_List:
#     if x > gretest_number:
#         gretest_number = x
# print(gretest_number)

data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}

print(json.dumps(data))
# done