# num = int(input("what num u wan: "))
# if (num %3 == 0 and num %5 == 0):
#     print("this num is divisible by 3 and 5")
# else:
#     print("this num is not divisible by 3 and 5")

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# visitors = 0
# while visitors < 51:
#     print(visitors)
#     visitors += 1

# visitors = int(input("visitors alr present: "))
# maxv = int(input("max visitors allowed"))
# while visitors < maxv:
#     visitors += 1 
#     print(visitors)

# while True:
#     print("hi")
#     break

# visitors = 0
# while True:
#     visitors += 1 
#     print(visitors)
#     if visitors == 30:
#         break

# order = ""
# while True:
#     orders = input("what is your order: ")
#     if orders == "end":
#             break
#     else:
#         if order == "":
#               order = order + orders
#         else:
#              order = order + ", "+ orders



# num = 10
# while num > 0:
#     print(num)
#     num -= 1
#     if num ==5:
#          break
# else:
#     print("happy new year")
score = 0
count = 10
ans = int(0)
import random
while True:
    num1 = str(random.randint(0,200))
    num2 = str(random.randint(0,200))
    ans = input("what is " + num1 + " + " + num2 + ": " )
    if int(ans) == (int(num1) + int(num2)):
        print("u did it")
        score += 1
    else:
        print("wrong! try again")
    count -= 1
    if count == 0:
        break
print("you have scored " + str(score))



     