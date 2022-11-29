postfix = "23*456-*+"
postfix = "23*456-8/*+"
# postfix = "12+345+**"

stack   = []

operators = ['(',')','/','*','+','-']
operands  = ['0','1','2','3','4','5','6','7','8','9']

for ele in postfix:
	if ele in operands:
		stack.append(ele)
	else:
		a = float(stack[-1])
		del stack[-1]
		
		b = float(stack[-1])
		del stack[-1]

		if ele == '/':
			stack.append(b/a)
		elif ele == '*':
			stack.append(a*b)
		elif ele == '+':
			stack.append(a+b)
		else:
			stack.append(b-a)

print(stack[-1])