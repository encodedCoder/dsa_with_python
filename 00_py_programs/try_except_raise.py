try:
	num = int(input("Enter a +ve number: "))
	if num <= 0:
		raise ValueError("Error: not a +ve number.")
except ValueError as e:
	print(e)
except(ValueError):
	print("Most likey this is not a number")