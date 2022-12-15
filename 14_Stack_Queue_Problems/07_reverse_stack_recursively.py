def insert(stack, val):
    if stack:
        a = stack.pop()
        insert(stack, val)
        stack.append(a)
    else:
        stack.append(val)

def reverse(stack):
    if stack:
        a = stack.pop()
        reverse(stack)
        insert(stack, a)

stack = [1, 2, 3, 4,  5, 6, 7, 8, 9]
print(stack)

reverse(stack)
print(stack)