str = 'python program to sort word in alphabetical order'

words = str.split()

words.sort()

print(words)

for i in range(0, len(words)):
    words[i] = words[i].upper()

print(words[0].upper())

print(words)