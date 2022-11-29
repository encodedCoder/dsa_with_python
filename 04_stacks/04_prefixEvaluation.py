prefix = "+*23*4-56"
prefix = "+*23*4/-568"

stack   = []

operators = ['(',')','/','*','+','-']
operands  = ['0','1','2','3','4','5','6','7','8','9']

for i in range(len(prefix)-1, -1, -1):
	if prefix[i] in operands:
		stack.append(prefix[i])
	else:
		a = float(stack[-1])
		del stack[-1]
		
		b = float(stack[-1])
		del stack[-1]

		if prefix[i] == '/':
			stack.append(a/b)
		elif prefix[i] == '*':
			stack.append(a*b)
		elif prefix[i] == '+':
			stack.append(a+b)
		else:
			stack.append(a-b)

print(stack[-1])