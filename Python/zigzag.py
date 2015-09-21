__author__ = 'ZHIXU'

# this is the leetcode problem set, which is not the DP programming contest
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
# like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows:
            return s
        inputStrList = list(s)
        outputList = []
        for _ in range(numRows):
            outputList.append([])
        strIndex = 0
        posIndex = 0
        colIndex = 0
        while True:
            # deal with the case when colIndex is odd number
            if colIndex % 2 == 0:
                outputList[posIndex%numRows].append(inputStrList[strIndex])
                posIndex += 1
                strIndex += 1
                if posIndex % numRows == 0:
                    colIndex += 1
            # else colIndex is even, we need to ignore the append for 2 cases
            else:
                if posIndex % numRows == 0:
                    posIndex += 1
                elif posIndex % numRows == numRows-1:
                    posIndex += 1
                    colIndex += 1
                else:
                    outputList[posIndex%numRows].append(inputStrList[strIndex])
                    posIndex += 1
                    strIndex += 1
            if strIndex == len(inputStrList):
                break
        outputStr = ''
        for i in xrange(len(outputList)):
            for j in xrange(len(outputList[i])):
                outputStr += outputList[i][j]
        return outputStr


if __name__ == '__main__':
    sol = Solution()
    inputStr = 'PAYPALISHIRING'
    print(inputStr)
    print sol.convert(inputStr, 3)
