def rotate(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    
def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1


nums = [1,2,3,4,5,6,7]
rotate(nums, 11)
print(nums)