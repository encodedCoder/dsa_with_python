def is_prime(num):
	i = 2
	while i**2 <= num:
		if num%i == 0:
			return False
		i += 1
	return True



for i in range(20, 40):
	if is_prime(i):
		print(i)