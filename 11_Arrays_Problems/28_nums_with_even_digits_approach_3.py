def findNumbers(nums):
    count = 0
    return sum([1 for ele in nums if len(str(ele))%2 == 0])


nums = [12,345,2,6,7896]
# nums = [555,901,482,1771]
print(findNumbers(nums))