# def pushDominoes(self, dominoes: str) -> str:
class Solution:
    def pushDominoes(self, dominoes):
        n = len(dominoes)

        left = []
        leftFound = False
        for i in range(n-1, -1, -1):
            if not leftFound and dominoes[i] in ['.', 'R']:
                left.append(0)

            elif leftFound: 
                if dominoes[i] == '.':
                    left.append(left[-1]-1)
                elif dominoes[i] == 'L':
                    left.append(n)
                elif dominoes[i] == 'R': 
                    left.append(0)
                    leftFound = False

            elif dominoes[i] == 'L':
                left.append(n)
                leftFound = True

            elif dominoes[i] == 'R':
                left.append(0)
                leftFound = False
        left.reverse()

        right = []
        rightFound = False
        for i in range(n):
            if not rightFound and dominoes[i] in ['.', 'L']:
                right.append(0)

            elif rightFound: 
                if dominoes[i] == '.':
                    right.append(right[-1]-1)
                elif dominoes[i] == 'R':
                    right.append(n)
                elif dominoes[i] == 'L': 
                    right.append(0)
                    rightFound = False

            elif dominoes[i] == 'R':
                right.append(n)
                rightFound = True

            elif dominoes[i] == 'L':
                right.append(0)
                rightFound = False

        result = []
        for i in range(n):
            if left[i] == right[i]:
                result.append('.')
            elif left[i] > right[i]:
                result.append('L')
            else:
                result.append('R')


        # print(result)
        result = ''.join(result)
        return result


dominoes = ".L.R...LR..L.."
# output = "LL.RR.LLRRLL.."

dominoes = "RR.L"
# output = "RR.L"

print(Solution.pushDominoes(0, dominoes))