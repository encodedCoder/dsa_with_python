lst = [1,2,3,4,5,6]

index = 0; sum = 0
while index<len(lst):
    sum += lst[index]
    index += 1
    if index == 5:
        break
else:
    print("No item in list")

print(sum)