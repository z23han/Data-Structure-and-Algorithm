__author__ = 'ZHIXU'

# given a m x n matrix, if an element is 0, set its entire row and column to be 0.

import random


class GenMatrix:
    def __init__(self, row, col):
        self.mat = []
        for i in xrange(row):
            subMat = []
            for j in xrange(col):
                subMat.append(random.randint(0,20))
            self.mat.append(subMat)

    def __print__(self):
        for i in xrange(len(self.mat)):
            print(self.mat[i])
        return


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    # here I would simply use the dumbest method
    def setZeroes(self, matrix):
        firstRow = -1
        firstCol = -1
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j == 0:
                        firstCol = 1
                    if i == 0:
                        firstRow = 1
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRow == 1:
            for i in xrange(len(matrix[0])):
                matrix[0][i] = 0

        if firstCol == 1:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0
        return


if __name__ == '__main__':
    inst = GenMatrix(10, 10)
    print("Old matrix")
    inst.__print__()
    sol = Solution()
    sol.setZeroes(inst.mat)
    print("")
    print("New matrix")
    inst.__print__()
