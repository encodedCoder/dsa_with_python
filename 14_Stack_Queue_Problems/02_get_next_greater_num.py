nums   = [15,12,16,2,1,0,7,8]
stack  = []
result = []

i = len(nums)-1
while i >= 0:
    if not stack:
        stack.append(-1)
        result.append(-1)
    elif nums[i] < nums[i+1]:
        stack.append(nums[i+1])
        result.append(nums[i+1])
    elif nums[i] > nums[i+1]:
        while stack and nums[i] > stack[-1]:
            del stack[-1]
        else:
            if stack:
                result.append(stack[-1])
            else:
                stack.append(-1)
                result.append(-1)
    i -= 1

print(stack)
result.reverse()
print(result)