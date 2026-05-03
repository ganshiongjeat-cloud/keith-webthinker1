# import random
# user = 0
# list = []
# for i in range(5):
#     user = (random.randint(1, 6))
#     user.append(list)
# print(list)

# fruits = ["apple", "banana", "cherry", "durian"]
# price = ["2", "3", "5", "10"]
# for i in range(len(fruits)):
#     print(fruits[i] + "cost $" + price[i])

# status = ""
# items = ["apple", "milk", "bread", "egg", "chocolate"]
# stock = [15, 0, 8, 25, 3]
# for i in range(len(items)):
#     if stock[i] == 0:
#         status = "out of stock"
#     elif stock[i] < 10:
#         status = "low stock"
#     else:
#         status = "well stocked"
#     print("item: " + items[i] + "| Qty: " + str(stock[i]) + "| Status: " + status)

# while True:
#     check_stock = input("check stock for which item: ")
#     for i in range(len(items)):
#         if items[i] == check_stock:
#             print("Result: We have " + str(stock[i]) + " " + items[i] + " remaining")
# else:
#     print("Error: item not found in database")






shopping_list = ["pens", "pencils", "erasers", "notebooks"]
print(shopping_list)
counter = input("how many more items should i buy")
for i in range(len(counter)):
    item = input("what item should i buy")
    shopping_list.append(item)
print(shopping_list)

  



