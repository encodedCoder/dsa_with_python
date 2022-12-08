def findDuplicates(nums):
    seen    = set()
    result  = [] 
    for ele in nums:
        if ele not in seen: seen.add(ele)
        else: result.append(ele)
    return result


nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))