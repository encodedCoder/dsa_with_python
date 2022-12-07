def findNumbers(nums):
    nums_len = len(nums)

    count = 0
    for i in range(nums_len):
        tempNum = nums[i]
        digitCount = 0
        while tempNum:
            tempNum //= 10
            digitCount += 1
        if digitCount >= 2 and digitCount%2 == 0:
            count += 1

    return count




nums = [12,345,2,6,7896]
nums = [555,901,482,1771]
print(findNumbers(nums))