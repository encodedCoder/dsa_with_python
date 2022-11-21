def hcf(num1, num2):
	if num1 == num2:
		return num1
	elif num1 < num2:
		temp = num1
	else:
		temp = num2
	while temp:
		if not num1%temp and not num2%temp:
			return temp
		temp = temp - 1

print(hcf(80))