__author__ = 'ZHIXU'

import random


class ArrayGeneration:
    def __init__(self, length):
        self.arr = []
        for i in xrange(length):
            num = random.randint(1, 100)
            # we need distinct numbers in the arr
            while True:
                if num not in self.arr:
                    self.arr.append(num)
                    break
                else:
                    num = random.randint(1, 100)

    def sortedArray(self):
        return sorted(self.arr)

    def rotatedArray(self, pivot):
        original = self.sortedArray()
        return original[pivot:]+original[:pivot]


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        return self.helper(0, len(nums)-1, nums, target)

    def switchSorted(self, nums):
        starting = self.find_pivot(0, len(nums)-1, nums)
        new_arr = nums[starting:]+nums[:starting]
        return new_arr

    def find_pivot(self, low, high, nums):
        assert high >= low, "high < low error!"
        if high == low:
            return low
        mid = (high + low)/2
        if mid < high and nums[mid] > nums[mid+1]:
            return mid+1
        if mid > low and nums[mid-1] > nums[mid]:
            return mid
        if nums[low] < nums[mid]:
            return self.find_pivot(mid+1, high, nums)
        else:
            return self.find_pivot(low, mid-1, nums)

    def helper(self, low, high, nums, target):
        if low == high:
            if nums[low] == target:
                return low
            else:
                return -1
        mid = (low + high) / 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if mid == 0:
                return -1
            return self.helper(low, mid-1, nums, target)
        else:
            if mid == len(nums)-1:
                return -1
            return self.helper(mid+1, high, nums, target)


if __name__ == '__main__':
    arrayInst =ArrayGeneration(10)
    sorted_arr = arrayInst.sortedArray()
    pivot = 4
    rotated_arr = arrayInst.rotatedArray(pivot)
    #print(sorted_arr)
    print(rotated_arr)
    target_index = random.randint(0, 9)
    target = rotated_arr[target_index]
    sol = Solution()
    new_arr = sol.switchSorted(rotated_arr)
    index = sol.search(new_arr, target)
    print(target)
    print(new_arr[index])