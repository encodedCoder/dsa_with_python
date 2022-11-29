infix   = "2*3+4*(5-6)"
infix   = "2*3+4*(5-6)/8"
infix   = "(1+2)*3*(4+5)"

postfix = []
stack   = [None]

operators = ['(',')','/','*','+','-']
operands  = ['0','1','2','3','4','5','6','7','8','9']

i = 0
while i < len(infix):
    if infix[i] in operands:
        postfix.append(infix[i])
        i += 1
    elif infix[i] in operators:
        if stack[-1] == None:
            stack.append(infix[i])
            i += 1

        elif infix[i] == '(':
            stack.append(infix[i])
            i += 1

        elif infix[i] == ')':
            while stack[-1] != '(':
                postfix.append(stack[-1])
                del stack[-1]
            del stack[-1]
            i += 1

        elif infix[i] == '/':
            if stack[-1] in ['(','/','*','+','-']:
                stack.append(infix[i])
                i += 1

        elif infix[i] == '*':
            if stack[-1] in ['(','*','+','-']:
                stack.append(infix[i])
                i += 1
            else:
                postfix.append(stack[-1])
                del stack[-1]

        elif infix[i] == '+':
            if stack[-1] in ['(','+','-'] :
                stack.append(infix[i])
                i += 1
            else:
                postfix.append(stack[-1])
                del stack[-1]


        elif infix[i] == '-':
            if stack[-1] in ['(','-']:
                stack.append(infix[i])
                i += 1
            else:
                postfix.append(stack[-1])
                del stack[-1]

while stack[-1]:
    postfix.append(stack[-1])
    del stack[-1]

postfix = ''.join(postfix)
print(postfix)