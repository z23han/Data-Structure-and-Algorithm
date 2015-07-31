# given a sorted array and a target value, return the index if the target is found. otherwise
# return the index where it would be if it were inserted in order.

import random

# generate an array with sorted order
class Array_Generate:
    def __init__(self):
        self.array = []
        for i in xrange(10):
            self.array.append(random.randint(1, 100))
        self.array.sort()


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert1(self, nums, target):
        if nums == []:
            return 0
        if target <= nums[0]:
            return 0
        if target == nums[len(nums)-1]:
            return len(nums)-1
        if target > nums[-1]:
            return len(nums)
        first = nums[0]
        for i in xrange(1, len(nums)):
            second = nums[i]
            if target <= second:
                return i
            else:
                first = second
        return 0

    def searchInsert2(self, nums, target):
        return self.helper(0, len(nums)-1, nums, target)

    def helper(self, low, high, nums, target):
        if low == high:
            if target > nums[low]:
                return low+1
            else:
                return low

        mid = (high - low)/2 + low

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            if mid == len(nums)-1:
                return mid+1
            elif target == nums[mid+1]:
                return mid+1
            elif target < nums[mid+1]:
                return mid+1
            else:
                return self.helper(mid+1, high, nums, target)
        else:
            if mid == 0:
                return 0
            elif target == nums[mid-1]:
                return mid-1
            elif target > nums[mid-1]:
                return mid
            else:
                return self.helper(low, mid-1, nums, target)


if __name__ == '__main__':
    arr = Array_Generate()
    print 'original array', str(arr)
    sol = Solution()
    target = random.randint(1, 100)
    print 'target', str(target)
    print sol.searchInsert1(arr.array, target)
    print sol.searchInsert2(arr.array, target)