def almostSorted(nums):
    nums_len = len(nums)

    # find if sorted array
    for i in range(nums_len-1):
        if nums[i] > nums[i+1]:
            break
        i += 1
    else:
        print('yes')
        return 

    # find the anamoly
    i = 0; j = 0; count = 0
    while i < len(arr)-1:
        if nums[i] > nums[i+1] and not count:
            return anamoly(nums, i, nums_len-1)
            count += 1
        i += 1
    print('no')
    return

def anamoly(nums, i, j):
    if i+2 <= j:
        if nums[i+1] > nums[i+2]:
            k = i+1
            while k < j:
                if nums[k] > nums[k+1]:
                    k += 1
                

    


arr = [1, 5, 4, 3, 2, 6]
arr = [1, 2, 3, 4, 5, 6]
arr = [1, 2, 3, 4, 6, 5]
almostSorted(arr)
