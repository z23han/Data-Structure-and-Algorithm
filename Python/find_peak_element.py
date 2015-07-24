import random

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.head = None

    def __insert__(self, node):
        current_node = self.head
        if current_node == None:
            self.head = node
            return
        while True:
            if current_node.data <= node.data:
                if current_node.right == None:
                    current_node.right = node
                    return
                else:
                    current_node = current_node.right
            else:
                if current_node.left == None:
                    current_node.left = node
                    return
                else:
                    current_node = current_node.left

    def __printTree__(self, print_node):
        if print_node == None:
            return
        else:
            self.__printTree__(print_node.left)
            print print_node.data
            self.__printTree__(print_node.right)


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        return self.findPeakUntil(nums, 0, len(nums)-1)

    def findPeakUntil(self, testNums, low, high):
        mid = low + (high - low) / 2
        if (mid == 0 or testNums[mid-1] <= testNums[mid]) and \
            (mid == len(testNums)-1 or testNums[mid+1] <= testNums[mid]):
            return mid
        elif mid > 0 and testNums[mid-1] >= testNums[mid]:
            return self.findPeakUntil(testNums, low, mid-1)
        else:
            return self.findPeakUntil(testNums, mid+1, high)





if __name__ == '__main__':
    data_list = []
    for i in xrange(10):
        d = random.randint(1, 100)
        data_list.append(d)
    print data_list
    sol = Solution()
    print sol.findPeakElement(data_list)
