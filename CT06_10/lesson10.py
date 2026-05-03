# print("Hello from lesson 10")
import random
# number = random.randint(1,15)
# user = input("choose a num from 1 to 15")
# chance = 3
# for i in range(4):
#     if chance!=0:
#         if (number == user):
#             print("correct!")
#             break
#         else:
#             chance -=1


# num = input("gimme a number: ")
# if (int(num) > 0):
#     print(str(num) + " is a positive number ")
# else:
#     print(str(num) + " is a negative number")

# password = random.randint(1,1000)
# user = input("what is the password, its a number: ")
# if (int(password) == int(user)):
#     print("login successful")
# else:
#     print ("Ur GAy")

# age = input("what is your age: ")
# if (int(age) < 13):
#     print("child")
# else:
#     if (int(age) < 19):
#         print("teenager")
#     else:
#         print("adult")

# temp = input("what is the temperature outside? ")
# if (int(temp) > 30):
#     print("go swimming")
# elif (int(temp) > 24):
#         print("go play basketball")
# elif (int(temp) > 19):
#     print("go cycling")
# else:
#     print("read indoors")

score = input("what is your score? ")
if (int(score) > 90):
     print("A")
elif (int(score) > 79):
     print("B")
elif (int(score) > 69):
     print("C")
else:
     print("F")

age = input("what is ur age ")
if (int(age) < 1):
    print("age cannot be negative")
elif (int(age) < 18):
    print("not elligible to vote")
else:
     print("elligible to vote")

money = input("how much angpao money u got")
if (int(money) > 149):
     print("u can buy a gaming keyboard")
elif (int(money) > 99):
     print("u can buy a new game")
elif (int(money) > 49):
     print("u can buy a gaming mouse")
elif (int(money) > 19):
     print("u can buy a gaming mouse pad")
else:
     print("snacks are all u can afford")