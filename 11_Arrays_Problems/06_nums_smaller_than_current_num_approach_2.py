def count_smaller_nums(nums):
    sorted_nums = sorted(nums)

    count_hash = {}
    for i in range(len(sorted_nums)):
        if sorted_nums[i] not in count_hash:
            count_hash[sorted_nums[i]] = i

    count_lst = []
    for i in range(len(nums)):
        count = count_hash[nums[i]]
        count_lst.append(count)

    return count_lst


nums = [5, 8, 3, 6, 4]
nums = [8, 1, 2, 2, 3]
nums = [7, 7, 7, 7]
nums = [44,39,69,51,43,100,93,87,73,63,14,82,48,48,26,71,0,35,81,76,92,94,93,65,25,59,76,66,52,95,91,39,89,21,57,79,85,67]
print(count_smaller_nums(nums))