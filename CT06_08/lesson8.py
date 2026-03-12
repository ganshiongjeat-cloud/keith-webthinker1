# Recap 1
# total = 1
# for i in range(1 , 6):
#     num = input("what will number " + str(i) + (" be??? "))
#     total = int(total) * int(num)
# print("the result is " + str(total))

import time

# for i in range(10 , 0 , -1):
#     print(i)
#     time.sleep(1)

import random

# random_num = random.randint(1 , 10)
# yournum = input("pick a number from 1 to 10 ")
# if  (int(yournum) == int(random_num)):
#     print("jackpot!!!")
# else:
#     print("you just lost a lot of moneyyyyy!")

# random_num = random.randint(1 , 1000)
# random_num1 = random.randint(1 , 100)
# answer = random_num + random_num1
# userans = int(input("what is " + str(random_num) + "+ " + str(random_num1) + "?\n"))
# if userans == answer:
#     print("correct!")
# else:
#     print("incorrect! u suck.")

score = 0
howmany = input("how many questions u wan")
howmany = int(howmany)
for i in range(howmany):
    random_num = random.randint(1 , 10)
    random_num1 = random.randint(1 , 100)
    answer = random_num * random_num1
    userans = int(input("what is " + str(random_num) + " x " + str(random_num1) + "?\n"))
    if userans == answer:
        print("correct!")
        score = int(score) + 1
    else:
        print("incorrect! u actually suck bre.")

print("you got " + str(score) + " out of " + str(howmany))

number = int(input("gimme a num "))
if number % 2 == 0:
    print("even number is this ")
else:
    print("odd number is this ")

num1 = int(input("gimme a num"))
num2 = int(input("another num pls"))
if num2 % num1 == 0:
    print("true")
else:
    print("false")





