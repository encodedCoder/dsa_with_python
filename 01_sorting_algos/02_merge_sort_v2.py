def merge(lst, lst1, lst2):
    i = 0
    j = 0
    k = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst[k] = lst1[i]
            i = i + 1
            k = k + 1
        elif lst1[i] > lst2[j]:
            lst[k] = lst2[j]
            j = j + 1
            k = k + 1
    if i < len(lst1):
        while i < len(lst1):
            lst[k] = lst1[i]
            k = k + 1
            i = i + 1
    elif j < len(lst2):
        while j < len(lst2):
            lst[k] = lst2[j]
            k = k + 1
            j = j + 1


def merge_sort(lst):
    if len(lst) > 1:
        lst_half = len(lst) // 2
        lst1 = lst[:lst_half]
        lst2 = lst[lst_half:]
        merge_sort(lst1)
        merge_sort(lst2)
        merge(lst, lst1, lst2)


lst = [4, 2, 3, 5, 7, 8, 6, 9]
print(lst)
merge_sort(lst)
print(lst)
