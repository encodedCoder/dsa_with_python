def bubble_sort(lst):
    j = 1
    swap = True
    while j < len(lst)-1:
        i = 0
        if swap:
            swap = False
            while i < len(lst) - j:
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    swap = True
                i = i + 1
        j = j + 1
        

lst = [4, 2, 3, 6, 8, 7, 5, 9]
print(lst)
bubble_sort(lst)
print(lst)
