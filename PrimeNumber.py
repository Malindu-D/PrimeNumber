from math import sqrt
num = int(input("Enter a Number: "))

if num <= 1:
    print(num, "is a Not Prime Number")
elif num == 2:
    print(num, "is a Prime Number")
else:
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            print(num, "is a Not Prime Number")
            break
    else:
        print(num, "is a Prime Number")
