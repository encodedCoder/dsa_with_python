num1 = 11; num2 = 2; num3 = 8

largest = 0

if num1 > num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
elif num2 > num3:
    largest = num2

print("Largest among {0}, {1} and {2} is: {3}".format(num1, num2, num3, largest))

