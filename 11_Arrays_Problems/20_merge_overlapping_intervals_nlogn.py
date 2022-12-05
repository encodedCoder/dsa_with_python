def merge(intervals):
    merge_sort(intervals)
    print(intervals)

    start_i = intervals[0][0]
    end_i   = intervals[0][1]

    merged_intervals = []
    for i in range(len(intervals)-1):
        if end_i >= intervals[i+1][0]:
            start_i = min(start_i, intervals[i+1][0])
            end_i   = max(end_i, intervals[i+1][1])
        else:
            merged_intervals.append([start_i,end_i])
            start_i = intervals[i+1][0]
            end_i   = intervals[i+1][1]
    merged_intervals.append([start_i,end_i])

    return merged_intervals

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        lst_1 = lst[:mid]
        lst_2 = lst[mid:]
        merge_sort(lst_1)
        merge_sort(lst_2)
        merge_lsts(lst, lst_1, lst_2)

def merge_lsts(lst, lst_1, lst_2):
    i = j = k = 0
    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i][0] <= lst_2[j][0]:
            lst[k] = lst_1[i]
            i += 1
            k += 1
        else:
            lst[k] = lst_2[j]
            j += 1
            k += 1

    while i < len(lst_1):
        lst[k] = lst_1[i]
        i += 1
        k += 1

    while j < len(lst_2):
        lst[k] = lst_2[j]
        j += 1
        k += 1


intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[0,4]]
# intervals = [[1,4],[0,1]]
# intervals = [[1,4],[0,0]]
# intervals = [[0,2],[1,5],[6,8],[8,9]]
intervals = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
print(merge(intervals))