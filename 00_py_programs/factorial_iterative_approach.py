def factorial(num):
	fact = num
	while num > 1:
		num -= 1
		fact *= num
	return fact

print(factorial(5)) 