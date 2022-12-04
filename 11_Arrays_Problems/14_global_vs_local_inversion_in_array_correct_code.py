def inversions(nums):
    # calculate local inversions
    local_inversion = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            local_inversion += 1

    # calculate global inversions
    nums_copy = nums.copy()
    merge_sort(nums_copy)

    return global_inversions == local_inversion


def merge_sort(lst):
    if len(lst)>1:
        mid   = len(lst) // 2
        lst_1 = lst[:mid]
        lst_2 = lst[mid:]
        merge_sort(lst_1)
        merge_sort(lst_2)
        merge(lst, lst_1, lst_2)

def merge(lst, lst_1, lst_2):
    global global_inversions
    i = 0
    j = 0
    k = 0
    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] < lst_2[j]:
            lst[k] = lst_1[i]
            i += 1
            k += 1
        else:
            lst[k] = lst_2[j]
            j += 1
            k += 1
            global_inversions += (len(lst_1) - i)

    while i < len(lst_1):
        lst[k] = lst_1[i]
        i += 1
        k += 1

    while j < len(lst_2):
        lst[k] = lst_2[j]
        j += 1
        k += 1



global_inversions = 0


# A = [1, 0, 2]
# A = [1, 2, 0]
# A = [0, 2, 1]
# A = [1, 0]
# A = [2, 1, 0]
# A = [0, 1, 2]
# A = [1,0]
A = [0, 1, 2]
A = [1,5,2,6,3,0]
A = [4, 6, 1, 7, 3, 2, 5]
A = [7, 5, 1, 3, 4, 6]
print(inversions(A))
print(global_inversions)