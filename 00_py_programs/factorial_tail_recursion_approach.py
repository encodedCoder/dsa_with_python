def factorial_tail_recusrion(num, accumulator):
	if num in (0, 1):
		return accumulator
	else:
		return factorial_tail_recusrion(num-1, num * accumulator)


print(factorial_tail_recusrion(6, 1))