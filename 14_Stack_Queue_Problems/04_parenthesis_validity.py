class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None]
        for ele in s:
            if ele in ['(', '[', '{']:
                stack.append(ele)
            elif ele == ')' and stack[-1] == '(':
                del stack[-1]
            elif ele == ']' and stack[-1] == '[':
                del stack[-1]
            elif ele == '}' and stack[-1] == '{':
                del stack[-1]
            else:
                break
        if stack[-1] == None:
            return True
        else:
            return False