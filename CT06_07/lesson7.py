print("Hello from lesson 7")

for i in range(1 , 11):
    print (i)

for i in range(2 , 21 , 2):
    print(i)

for i in range(11 , 0 , -1):
    print(i)

words = input("what do u want to repeat")
times = input("number of times")
for i in range(int(times)):
    print(words)

name = input("what is ur name")
num = input("how many times you want repeat")
for i in range(int(num)):
    print("nice to meet you " + name)

sum = 0
for i in range(5):
    ask = input("what is number#" + str(i))
    sum += int(ask)
print(sum)

userb = input("what number's timetable u wan")
for i in range(1 , 13):
    #print(int(ask) * int(i))
    print(str(i) + "x" + str(userb) + "=" + str(i*int(userb)))

sum = 0
for i in range(5):
    ask = input("what is ur marks")
    sum += int(ask)
average = sum/5
print(average)










