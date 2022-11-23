str = 'vcabbacV'

str = str.upper()

reveredStr = reversed(str)

if list(str) == list(reveredStr):
    print('Yes, given string is apalindrome')
else:
    print('No, given string is not a palindrome')