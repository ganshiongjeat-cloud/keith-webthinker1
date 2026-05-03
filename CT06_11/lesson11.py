# price = input("what is the cost of the item? ")
# if (int(price) <= 5):
#     print("Sounds good.")
# elif (int(price) <= 50):
#     print("are you sure about that? ")
# elif (int(price) <= 500):
#     print("money doesnt rain from the sky uk")
# else:
#     print("rich kid. :(")

# rider1 = 125
# rider2 = 150
# if rider1 and rider2 > 120:
#     print("ur allowed")
# else:
#     print("get out")

# num = input("gimme a number")
# if int(num) % 3 == 0 and int(num) % 7 == 0:
#     print("the num is divisible by 3 and 7")
# else:
#     print("nothing happens!")

# name1 = ("what is your first name")
# name2 = ("what ur last name? ")
# if str(name1) == ("james") and str(name2) == ("leong"):
#     print("youre wanted")

age = input("what is your age")
if int(age) <= 12 or int(age) >= 65:
    print("15 dolla for 1 ticket")
else:
    print("20 dolla per ticket")

gender = input("what is your gender: ")
if gender == ("M") or gender == ("male"):
    print("valid input")
else:
    print("invalid input")

colour = input("gimme a colour: ")
if colour != "green":
    print("try again")
    colour = input("gimme a colour: ")

day = input("what day is it ")
if day != "saturday":
    print("GeT BAcK To WoRK")

password = input("whats the password: ")
if password != "Python123":
    print("access denied.")

burger = input("u want burger?yes or no ")
fries = input("u want fries?yes or no ")
drink = input("u want drink?yes or no ")
if burger == "yes" and fries == "yes" and drink == "no":
    print("won't u get thirsty")

gamestatus = input("enter game status ")
if gamestatus =="active" or not gamestatus == "pause":
    print("game in progress")
else:
    print("game is paused and inactive")
