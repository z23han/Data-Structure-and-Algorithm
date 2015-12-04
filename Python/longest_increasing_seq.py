'''
Given an unsorted array of integers, find the length of longest increasing sub-sequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing sub-sequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

#dynamic programming, binary search
'''

import random

def seq_generation(num):
    return [random.randint(1, 100) for _ in range(num)]


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        L = [1] * len(nums)
        for i in range(1, len(L)):
            maxN = 0
            for j in range(i):
                if nums[j] > nums[i] and L[j] > maxN:
                    maxN = L[j]
            L[i] = maxN + 1
        maxI = 0
        for i in range(len(L)):
            if L[i] > maxI:
                maxI = L[i]
        return maxI
        '''
        maxLength = 1
        bestEnd = 0
        DP = [1] * len(nums)
        prev = [-1] * len(nums)

        for i in range(1, len(nums)):

            for j in range(i-1, -1, -1):
                if DP[j]+1 > DP[i] and nums[j] < nums[i]:
                    DP[i] = DP[j] + 1
                    prev[i] = j
            if DP[i] > maxLength:
                bestEnd = i
                maxLength = DP[i]
        print DP
        print prev
        return maxLength



if __name__ == '__main__':
    seq = seq_generation(10)
    print seq
    sol = Solution()
    print sol.lengthOfLIS(seq)



