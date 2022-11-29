def binary_search(arr, lowerBound, upperBound, x):
    if upperBound >= lowerBound:
        mid = (lowerBound + upperBound)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, lowerBound, mid-1, x)
        else:
            return binary_search(arr, mid+1, upperBound, x)
    else:
        return -1

arr = [1, 3, 5, 6, 7, 9, 10]
x = 9

result = binary_search(arr, 0, len(arr)-1, x)

print(arr)
if result != -1:
    print("Element found at index: ", str(result))
else:
    print("Element not present.")