def two_repeating_elements(nums):
    n = len(nums)

    xor = 0
    for i in range(n):
        xor ^= nums[i]
    for i in range(n-1):
        xor ^= i

    shifting_1 = 1
    while True:
        if xor & shifting_1:
            break
        shifting_1 <<= 1

    num_1 = 0
    for i in range(n):
        if shifting_1 & nums[i]:
            num_1 ^= nums[i]
    for i in range(n-1):
        if shifting_1 & i:
            num_1 ^= i

    num_2 = xor ^ num_1

    return num_1, num_2

nums = [1, 2, 3, 3, 4, 5, 5, 6] 
nums = [2, 4, 3, 1, 2, 5, 4]
nums = [4, 2, 4, 5, 3, 3, 1]
print(two_repeating_elements(nums))






