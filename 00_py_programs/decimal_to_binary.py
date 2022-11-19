def binary(decimal):
	binary_lst = []
	while decimal:
		binary_lst.append(str(decimal%2))
		decimal = decimal//2
	binary_lst = ''.join(binary_lst)
    return int(reversed(str(binary_lst)))
    
print("Binary value of {0} is: {1}".format(10, binary(10)))


