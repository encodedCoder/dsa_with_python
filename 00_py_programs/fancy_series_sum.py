'''
This program gives the sum of a series having 'n' terms which is represented by following recurrence relation
	A(n) = 6*(n^2) + 2*n + A(n-1)
'''

'''
Following program is implemented using tail recursion which can give us optimized usage of recursion stack
'''


def fancy_series_sum(num_of_terms, accumulation):
	if num_of_terms == 1:
		return accumulation + 8
	if num_of_terms > 1:
		return fancy_series_sum(num_of_terms-1, accumulation + 6*(num_of_terms**2) + 2*num_of_terms)


print(fancy_series_sum(99, 0))
