stack_size = 5
stack = [None]*stack_size

start = top_1 = 0
end   = top_2 = len(stack) - 1

def is_overflow():
	global top_1, top_2
	return top_1 == top_2

def push_in_stack_1(val):
	global top_1
	if is_overflow():
		print("Stack Overflow")
	else:
		stack[top_1] = val
		top_1 += 1

def push_in_stack_2(val):
	global top_2
	if is_overflow():
		print("Stack Overflow")
	else:
		stack[top_2] = val
		top_2 -= 1

def pop_from_stack_1():
	global start, top_1
	if stack[start] is None:
		print("\nStack_1 Underflow")
		return None
	elif top_1 == 0:
		val = stack[top_1]
		stack[top_1] = None
	else:
		top_1 -= 1
		val = stack[top_1]
		stack[top_1] = None
	return val

def pop_from_stack_2():
	global top_2, end
	if stack[end] is None:
		print("\nStack_2 Underflow")
		return None
	elif top_2 == end:
		val = stack[top_2]
		stack[top_2] = None
	else:
		top_2 += 1
		val = stack[top_2]
		stack[top_2] = None
	return val

print(stack)

push_in_stack_1(5)
push_in_stack_2(48)
push_in_stack_1(55)
push_in_stack_1(50)
pop_from_stack_2()
push_in_stack_2(58)
pop_from_stack_2()
pop_from_stack_2()
push_in_stack_2(64)


print(stack)
