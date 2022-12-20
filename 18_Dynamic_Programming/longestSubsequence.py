class Solution:
    def __init__(self):
        self.dp = {}
    def longestSubsequence(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if self.dp.get(s):
            return self.dp.get(s)
        if(int(s, 2) <= k):
            self.dp[s] = len(s)
            return len(s)
        maxLength = 0
        for i in range(len(s)):
            if s[i] == '1':
                currStr = s[:i] + s[i+1:]
                maxLength = max(self.longestSubsequence(currStr, k), maxLength)
                self.dp[currStr] = maxLength
        return maxLength


if __name__ == '__main__':
    s, k = '10101', 2
    s, k = '101011', 5
    s, k = '10010101', 5

    # s, k = '001010101011010100010101101010010', 93951055

    # s, k = "111100010000011101001110001111000000001011101111111110111000011111011000010101110100110110001111001001011001010011010000011111101001101000000101101001110110000111101011000101", 11713332

    # print(len(s))

    print(Solution().longestSubsequence(s, k))

    # for i in range(len(s)):
    #     print(s[:i] + s[i+1:])
