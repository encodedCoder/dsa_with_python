def replace_with_greatest_on_right(arr):
    lst = [0]*len(arr)
    lst[-1] = -1
    for i in range(len(arr)-1, 0, -1):
        if lst[i] > arr[i]:
            lst[i-1] = lst[i]
        else:
            lst[i-1] = arr[i]

    return lst


arr = [17,18,5,4,6,1]
# arr = [400]
print(replace_with_greatest_on_right(arr))