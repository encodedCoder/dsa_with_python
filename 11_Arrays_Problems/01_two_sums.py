'''
Problem link:-
	https://leetcode.com/problems/two-sum/
'''


def twoSum(nums, target):
    dict_1 = {}
    
    for i in range(len(nums)):
        val = target - nums[i]
        if dict_1.get(val):
            return [int(dict_1.get(target-nums[i])), i]
        else:
            if dict_1.get(nums[i]):
                continue
            else:
                dict_1[nums[i]] = str(i)

                
lst = [-3,4,3,90]
target = 0
print(twoSum(lst, target))