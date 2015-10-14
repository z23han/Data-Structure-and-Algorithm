__author__ = 'ZHIXU'

'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one.

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

import random

class Solution(object):
    # expensive method
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for i in xrange(1, len(nums)):
            numDict[i] = 0
        target = None
        for num in nums:
            if not numDict[num]:
                numDict[num] = 1
            else:
                target = num
                break
        return target


def generateNum(n):
    num = random.randint(1, n)
    pos = random.randint(0, n)
    numList = list(range(1, n))
    numList.insert(pos, num)
    random.shuffle(numList)
    return numList


if __name__ == '__main__':
    sol = Solution()
    nums = generateNum(20)
    target = sol.findDuplicate(nums)
    print nums
    print target

