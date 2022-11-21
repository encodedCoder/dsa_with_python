def fibonacci(term1, term2, terms):
	if terms >= 1:
		print(term1, end = ', ')
		terms -= 1
		fibonacci(term2, term1+term2, terms)

fibonacci(0, 1, 10)
	