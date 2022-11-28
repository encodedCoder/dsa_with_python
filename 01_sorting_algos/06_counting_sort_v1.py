def counting_sort(arr):
    length_of_arr = len(arr)
    max_ele = max(arr)
    count = [0]*(max_ele+1)
    output_arr = [0]*length_of_arr

    #1 - count the elements
    for i in range(length_of_arr):
        count[arr[i]] = count[arr[i]] + 1

    #2 - find the commulative count
    for i in range(1, max_ele+1):
        count[i] = count[i] + count[i-1]

    #3 - find the sorted output
    i = length_of_arr - 1
    while i >= 0:
        output_arr[count[arr[i]]-1] = arr[i]
        count[arr[i]] = count[arr[i]] - 1
        i = i - 1

    for i in range(length_of_arr):
        arr[i] = output_arr[i]

arr = [4,2,2,5,3,3,1]
counting_sort(arr)
print(arr)