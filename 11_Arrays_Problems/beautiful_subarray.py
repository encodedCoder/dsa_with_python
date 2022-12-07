def beautiful_subarray(arr, i):
    mid = None
    for i in range(i, len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        elif arr[i] < arr[i-1] and i != 1 :
            mid = arr[i-1]
            break
    if mid and i != len(arr)-1:
        return True, i+1
    else:    
        return False, i+1

testcases = int(input())

for i in range(testcases):
    current_array_length = int(input())
    current_array = input().split()
    current_array = [int(ele) for ele in current_array]

    beauty_count = 0
    i = 0
    while i < len(current_array):
        count, i = beautiful_subarray(current_array, i)
        print(count, ',', i)
        beauty_count += count
        
    print(beauty_count)