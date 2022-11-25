import math

count = 0

def do_something(num):
	global count
	count += 1
	if num <= 2 :
		print('1') 
		return 1
	else :
		print(math.sqrt(num))
		return (do_something(math.sqrt(num)))


# print("\n\n"do_something(1024), count)

do_something(1024)

