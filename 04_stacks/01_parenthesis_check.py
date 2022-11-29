parenthesis = "[{()()[]}][]))"
parenthesis = "{33+4*(4+6)+[5+8)]}"

stack = [None]
for ele in parenthesis:
    if ele in "{[(":
        stack.append(ele)
    elif ele in ")]}":
        if ele == ')' and stack[-1] == '(':
            del stack[-1]
        elif ele == ']' and stack[-1] == '[':
            del stack[-1]
        elif ele == '}' and stack[-1] == '{':
            del stack[-1]
        elif not stack[-1]:
            stack.append(ele)
        else:
            break

if not stack[-1]:
    print("Correct")
else:
    print("Incorrect")