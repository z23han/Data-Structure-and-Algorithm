# find the minimum depth of a binary tree, which is the # of nodes along the shortest
# path from the node down to the nearest leaf node.

import random

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root == None:
            return 0
        nodes = []
        counts = []

        nodes.append(root)
        counts.append(1)

        while nodes != []:
            curr = nodes.pop(0)
            count = counts.pop(0)
            if curr.left != None:
                nodes.append(curr.left)
                counts.append(count+1)
            if curr.right != None:
                nodes.append(curr.right)
                counts.append(count+1)
            if curr.left == None and curr.right == None:
                return count

        return 0

if __name__ == '__main__':
    root = TreeNode(random.randint(1, 100))
    for i in xrange(10):
        root.left = TreeNode(random.randint(1, 100))
        root.right = TreeNode(random.randint(1, 100))
        if random.randint(0, 1) == 0:
            root = root.left
        else:
            root = root.right
    sol = Solution()
    print sol.minDepth(root)