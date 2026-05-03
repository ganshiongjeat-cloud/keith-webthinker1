import random 

# first = random.randint(1 , 6)
# second = random.randint(1 , 6)
# third = random.randint(1 , 6)
# print("first num: " + str(first))
# print("second num: " + str(second))
# print("third num: " + str(third))
# firstno = first %2 == 0
# secondno = second %2 == 0
# thirdno = third %2 == 0
# all = firstno == secondno == thirdno
# print("all numbers are even/odd: " + str(all))

# apples = input("how many apples u buying")
# price = (int(apples) * 2)
# if int(apples) > 10:
#     print("10% discount")
#     apples = int(price) * int(0.9)
#     print (str(apples))
# else:
#     print (str(price))


apples = input("how many apples u buying? ")
apple_price = int(apples) * 0.6
orange = input("how many oranges u buying? ")
orange_price = int(orange) * 0.9
if int(apples) > 5:
    print("10% discount on apples!")
    apple_price = int(apple_price) * 0.9
    print("cost of apples is: " + str(apple_price))
else:
    print("cost of apples is: " + str(apple_price))
if int(orange) > 5:
    print("10% discount on oranges!")
    orange_price = int(orange_price) * 0.9
    print ("cost of oranges is: " + str(orange_price))
else:
    print ("cost of oranges is: " + str(orange_price))
total = int(orange_price) + int(apple_price)
print("your total is $" + str(total))

