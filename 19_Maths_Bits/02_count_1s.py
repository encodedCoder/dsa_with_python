def hammingWeight(n):
    count = 0
    while n:
        count = count + (n & 1)
        n >>= 1
        
    return count


n = 0b00000000000000000000000000001011
# n = 0b00000000000000000000000010000000
# n = 0b11111111111111111111111111111101
print(hammingWeight(n))