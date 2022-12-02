def find_majority_using_moore_voting_algorithm(nums):
    voter = nums[0]
    votes = 1
    for i in range(1, len(nums)):
        if nums[i] == voter:
            votes += 1
        elif nums[i] != voter:
            if votes > 0:
                votes -= 1
            elif votes == 0:
                voter = nums[i]

    count = 0
    for i in range(len(nums)):
        if nums[i] == voter:
            count += 1

    if count > len(nums) // 2:
        return voter
    else:
        return None


nums = [1, 2, 2, 1, 3, 1, 1]
print(find_majority_using_moore_voting_algorithm(nums))

nums = [3, 5, 3]
print(find_majority_using_moore_voting_algorithm(nums))

nums = [6,6,6,7,7]
print(find_majority_using_moore_voting_algorithm(nums))

nums = [8,8,7,7,7]
print(find_majority_using_moore_voting_algorithm(nums))

nums = [32,32,58,32,32,32,32,32,50,77,77,32,32,32,51,32,61,32,32,88,44,32,7,32,32,92,28,1,32,32,44,97,99,32,1,40,32,20,32,68,85,32,32,32,32,98,13,32,32,7,74,32,32,52,32,86,28,45,73,19,32,32,27,32,83,32,68,94,32,32,32,32,27,24,32,32,96,32,99,60,46,32,22,71,25,32,32,32,32,53,54,26,32,32,32,32,13,32,23,6]
print(find_majority_using_moore_voting_algorithm(nums))
