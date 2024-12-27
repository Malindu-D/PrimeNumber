num = int(input("Enter a Number: "))


if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0) and num !=0:
    print(num, "is a Not Prime Number")
else:
    print(num, "is a Prime Number")
