__author__ = 'ZHIXU'

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the
# bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

import random

# generate mxn grids
def generateGrids(m, n):
    grids = []
    for i in xrange(m):
        row = []
        for j in xrange(n):
            if i == 0 and j == 0:
                row.append(1)
            elif i == m-1 and j == n-1:
                row.append(1)
            else:
                row.append(random.randint(0,1))
        grids.append(row)
    return grids


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dynamic programming approach
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        dp = [[None for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            dp[i][0] = 1
        for j in xrange(n):
            dp[0][j] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

    def uniquePaths2(self, m, n):
        return self.dfs(0,0,m,n)

    def dfs(self, i, j, m, n):
        if i == m-1 and j == n-1:
            return 1

        if i < m-1 and j < n-1:
            return self.dfs(i+1,j,m,n) + self.dfs(i,j+1,m,n)

        if i < m-1:
            return self.dfs(i+1,j,m,n)

        if j < n-1:
            return self.dfs(i,j+1,m,n)

        return 0


if __name__ == '__main__':
    grids = generateGrids(10, 10)
    sol = Solution()
    num = sol.uniquePaths(5, 5)
    print num

