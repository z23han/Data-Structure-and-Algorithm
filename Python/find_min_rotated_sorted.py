class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, testNums, low, high):
        if low > high:
            raise ValueError('lower index is larger than upper index!')
        if high == low:
            return testNums[high]

        mid = low + (high - low) / 2
        if testNums[mid+1] <= testNums[mid]:
            return testNums[mid+1]
        if testNums[mid] <= testNums[mid-1]:
            return testNums[mid]
        if testNums[high] >= testNums[mid]:
            return self.helper(testNums, low, mid-1)
        else:
            return self.helper(testNums, mid+1, high)


if __name__ == '__main__':
    test_list = [4, 5, 6, 7, 8, 1, 2]
    sol = Solution()
    print sol.findMin(test_list)