class Solution:
    def printTriangle(self, N):
        for i in range(N):
            space=" "* i
            star="*"*(2*(N-i)-1)
            print(space+star)
