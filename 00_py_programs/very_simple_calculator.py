def sum(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

x = 12; y = 4
print('Sum of {0} and {1}: {2}'.format(x, y, sum(x, y)))
print('Subtract {0} and {1}: {2}'.format(x, y, subtract(x, y)))
print('Multiplication of {0} and {1}: {2}'.format(x, y, multiply(x, y)))
print('Divide {0} by {1}: {2}'.format(x, y, int(divide(x, y))))