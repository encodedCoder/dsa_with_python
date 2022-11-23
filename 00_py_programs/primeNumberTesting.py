num = int(input("Enter a number: "))

i = 2; isDivisible = False

while(i**2 <= num):
    if(num%i == 0):
        isDivisible = True
        print("{} is divisble by {}. Therfore".format(num, i))
        break
    i += 1

if isDivisible:
    print("{} is not prime number".format(num))
else:
    print("{} is a Prime number".format(num))