# out-of-place approach i.e. O(n) space complexity 

def even_parity_sort(nums):
    even_nums = []
    odd_nums = []

    for val in nums:
        if val % 2 == 0:
            even_nums.append(val)
        else:
            odd_nums.append(val)

    even_nums.extend(odd_nums)
    return even_nums

nums = [3,1,2,4]
print(even_parity_sort(nums))