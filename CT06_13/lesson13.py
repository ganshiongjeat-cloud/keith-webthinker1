import random
# num = 0
# counter = 0
# while num < 4 or num > 4:
#     counter += 1
#     num = random.randint(0 , 6)
#     print(num)
#     if counter == 0:
#         break
# print("number of tries to roll " + str(num) + "is " + str(counter))

# balance = 1000
# added = ""
# user = ""
# withdraw = ""
# while user != exit:
#     user = input("would u like to deposit, withdraw, check your balance or exit??? ")
#     if user == "deposit":
#         added = input("how much u want to deposit? ")
#         balance = balance + int(added)
#         print("transaction successful") 
#     elif user == "withdraw":
#         withdraw = input("how much u want withdraw? ")
#         balance = balance - int(withdraw)
#         print("transaction successful") 
#     elif user == "check balance":
#         print("your balance is " + str(balance))
#     else:
#         break

# groceries = ["apples" ,"bread" , "carrots", "dates", "egg", "flour", "grapes", "honey"]
# groceries[7] = "herbs"
# print(groceries)
# for i in groceries:
#     print(i)
# groceries.append("ice")
# print(groceries)
# groceries.insert(1,"banana")
# print(groceries)
# groceries.pop(2)
# print(groceries)

# for i in groceries:
#     if (i) == "apples":
#         print("apples: i need 5 of these")
#     elif (i) == "carrots":
#         print("carrots: i need 3 of these")
# grocery = []
# while True:
#     user = input("items bought ")
#     if user =="end":
#         break
#     grocery.append(user)

# for items in grocery:
#     print("I have bought " + items)
# print(grocery)

# grocery = []
# while True:
#     user = input("items bought ")
#     if user =="end":
#         break
#     grocery.append(user)

catalogue = ""
for i in catalogue:
    print(i)

user = input("whatt are you looking for")
if user in catalogue:
    print("yes we sell that")
else:
    print("sorry we dont sell that")


# lucky_num = []
# for i in range(10):
#     user =(random.randint(0,10000))
#     lucky_num.append(user)
# for i in len(lucky_num):
#     print("winner" + str(i + 1) + ": " + str(lucky_num))
    
pizzastuff = ["mushrooms", "pepperoni", "pineapple", "xtra cheese", "smoked duck", "ham"]
order = []
for i in range(len(pizzastuff)):
    print(str(i + 1) + ". " + pizzastuff[i])
while True:
    user = input("what pizza topping u 1?")
    if user != "end":
        order.append(user)
    else:
        break




