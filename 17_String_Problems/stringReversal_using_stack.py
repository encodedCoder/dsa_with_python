def reverse(S):
    lst = list(S)
    lst.reverse()
    S = ''.join(lst)
    return S

S = "Suresh"
print(reverse(S))