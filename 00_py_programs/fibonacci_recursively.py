def fibonacci(num1, num2, terms = 5):
    """
    This program prints the Fibonacci sequence
    """
    print(num1)
    if terms >= 2:
        return fibonacci(num2, num1 + num2, terms-1)

fibonacci(0, 1, 10)