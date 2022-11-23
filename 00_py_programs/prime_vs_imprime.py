def is_prime(num):
	i = 2
	while i**2 <= num:
		if num%i == 0:
			return False
		i += 1
	return True


print(is_prime(4))