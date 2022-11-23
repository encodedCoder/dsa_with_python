intervalStart = 10
intervalEnd = 50

for num in range(intervalStart, intervalEnd+1):
    isDivisible = False
    for index in range(2, num):
        if (num % index == 0):
            isDivisible = True 
            break
    if not isDivisible:
        print(num)