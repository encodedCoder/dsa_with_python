def factorial(num):
    '''
    This function returns the factorial of a number
    '''
    if num < 0:
        return False
    elif num > 1:
        return num * factorial(num-1)
    else:
        return 1

print(factorial(7))