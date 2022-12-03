def count_smaller_nums(nums):
    count_elements = [0]*101

    # count the individual elements
    for val in nums:
        count_elements[val] += 1

    # cummulative_count
    for i in range(1, 101):
        count_elements[i] += count_elements[i-1]


    # create the count_lst
    count_lst = []
    for val in nums:
        if val == 0:
            count_lst.append(0)
        else:
            count_lst.append(count_elements[val-1])

    return count_lst

# nums = [5, 8, 3, 6, 4]
nums = [8, 1, 2, 2, 3]
# nums = [7, 7, 7, 7]
nums = [44,39,69,51,43,100,93,87,73,63,14,82,48,48,26,71,0,35,81,76,92,94,93,65,25,59,76,66,52,95,91,39,89,21,57,79,85,67]
print(count_smaller_nums(nums))