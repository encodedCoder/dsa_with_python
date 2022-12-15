class Solution:
    def knows(self, M, a, b):
        return M[a][b]
    
    def celebrity(self, M, n):
        celeb = 0

        for i in range(n):
            if self.knows(M, celeb, i):
                celeb = i

        for i in range(n):
            if celeb == i:
                continue
            if self.knows(M, celeb, i) or not self.knows(M, i, celeb):
                return -1

        return celeb


if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)

        ob = Solution()
        print(ob.celebrity(m,n))