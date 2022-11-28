from pdb import set_trace

def counting_sort(lst, place):
    count_lst = [0]*10

    # Count the digits based on their "place"
    for i in range(len(lst)):
        count_index = (lst[i]//place)%10
        count_lst[count_index] += 1

    # Find the cummulative count
    for i in range(1, len(count_lst)):
        count_lst[i] += count_lst[i-1]

    output_lst = [0]*len(lst)
    # Apply the final stable counting sort
    for i in range(len(lst)-1, -1, -1):
        count_index = (lst[i]//place)%10
        output_lst[count_lst[count_index]-1] = lst[i]
#         set_trace()
        count_lst[count_index] -= 1

    for i in range(len(output_lst)):  
        lst[i] = output_lst[i]

        
def radix_sort(lst):
    max_ele = max(lst)
    place = 1
    while max_ele // place > 0:
        counting_sort(lst, place)
        place *= 10

arr = [329, 457, 657, 389, 436, 720, 355]
print(arr)
radix_sort(arr)
print(arr)