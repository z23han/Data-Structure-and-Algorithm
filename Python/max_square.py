__author__ = 'ZHIXU'

# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing all 1's and return its area.

import random


class Matrix:
    def __init__(self, length):
        self.length = length

    def mat(self):
        self.mat = []
        for i in xrange(self.length):
            subMat = []
            for j in xrange(self.length):
                subMat.append(random.randint(0, 1))
            self.mat.append(subMat)
        return self.mat

    def printMat(self):
        self.mat = self.mat()
        for i in xrange(self.length):
            print self.mat[i]

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare1(self, matrix):
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxVal = 0
        n = len(matrix)
        dp = []
        for i in xrange(n+1):
            subDp = []
            for j in xrange(n+1):
                subDp.append([])
            dp.append(subDp)
        print(dp)
        for i in xrange(1,n+1):
            for j in xrange(1,n+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                    maxVal = max(maxVal, dp[i][j])
        return maxVal*maxVal


if __name__== '__main__':
    matrix = Matrix(10)
    matrix.printMat()
    sol = Solution()
    print sol.maximalSquare1(matrix.mat)