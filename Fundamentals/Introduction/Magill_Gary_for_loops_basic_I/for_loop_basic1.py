#1-
for i in range(151):
    print(i)
#2-
for i in range(0,1005,5):
    print(i*5)
#3-
for i in range(1,101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

#4-
sum = 0
for i in range(0, 500,5):
    if i % 2 != 0:
        sum +=i

print(sum)

# #5-
for i in range(2018,0,-4):
    print(i)

# 6-
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1, 1):  # have to add (+1) onto "highNum" so that it goes to that number.
    if i % 3 == 0:
        print(i)


