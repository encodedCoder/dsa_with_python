'''
Solution_1 :- Hashing Based Solution.
			  Pros: O(n) Time Complexity
			  Cons: O(n) Space Complexity
'''
def using_hashing(nums):
	dict_1 = {}

	for i in range(len(nums)):
		dict_1[nums[i]] = 1

	max_num = max(nums) + 1
	for i in range(len(nums)):
		if not dict_1.get(max_num - nums[i]):
			return max_num - nums[i]



'''
Solution_2 :- Hashing Based Solution.
			  Pros: O(n) Time Complexity, O(1) Space Complexity
			  Cons: Overflow can occur if n is very large [n*(n+1)/2] 
'''
def addition_based_solution(nums):
	n = len(nums)+1
	sum__ = n*(n+1)//2
	for ele in nums:
		sum__ -= ele
	return sum__



'''
Solution_3 :- XOR based solution.
			  Pros: O(n) Time Complexity, O(1) Space Complexity
			  Cons: No problem at all.
'''
def xor_based_solution(nums):
	x1 = 1
	for i in range(2, len(nums)+2):
		x1 = x1^i

	x2 = 0
	for ele in nums:
		x2 = x2 ^ ele

	return x1^x2

nums = [1, 2, 5, 4, 6, 7, 9, 8, 10]
a = xor_based_solution(nums)
print(a)