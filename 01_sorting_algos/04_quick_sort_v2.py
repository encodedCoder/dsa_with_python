#There is something wrong with following imlementation
#Find out what's wrong with the following code.
#I also don't know.

def partition(lst):
    pivot = lst[-1]
    j = 0
    i = -1
    while j < len(lst)-1:
        if pivot > lst[j]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
        j += 1
    i += 1
    lst[i], lst[j] = lst[j], lst[i]
    return i


def quick_sort(lst):
    if len(lst) >= 1:
        i = partition(lst)
        quick_sort(lst[:i])
        quick_sort(lst[i+1:])

lst = [20, 69, 8, 21, 36, 57, 12, 42]
print(lst)
quick_sort(lst)
print(lst)
