'''
Given pre-order and in-order traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

# Tree, Array, Depth-first-search
'''

import random

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(numOfLeaves):
    leavesVal = [random.randint(1, 100) for _ in range(numOfLeaves)]
    treeNodes = [TreeNode(leavesVal[i]) for i in range(len(leavesVal))]
    return treeNodes


class Solution(object):
    def buildTree(self, preOrder, inOrder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preStart = 0
        preEnd = len(preOrder)-1
        inStart = 0
        inEnd = len(inOrder)-1

        return self.construct(preOrder=preOrder, preStart=preStart, preEnd=preEnd,
                              inOrder=inOrder, inStart=inStart, inEnd=inEnd)

    def construct(self, preOrder, preStart, preEnd, inOrder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None

        if preStart == preEnd or inStart == inEnd:
            rootIndex = inStart
            rootVal = preOrder[rootIndex]
            print 'rootIndex(inOrder):', str(rootIndex), 'rootVal:', str(rootVal)
            root = TreeNode(rootVal)
            root.left = None
            root.right = None
            return root

        rootVal = preOrder[preStart]
        root = TreeNode(rootVal)
        rootIndex = 0
        for i in range(len(inOrder)):
            if inOrder[i] == rootVal:
                rootIndex = i
                break
        print 'rootIndex(inOrder):', str(rootIndex), 'rootVal:', str(rootVal)

        root.left = self.construct(preOrder=preOrder, preStart=preStart+1, preEnd=preStart+(rootIndex-inStart),
                                   inOrder=inOrder, inStart=inStart, inEnd=rootIndex-1)
        root.right = self.construct(preOrder=preOrder, preStart=preStart+(rootIndex-inStart)+1, preEnd=preEnd,
                                    inOrder=inOrder, inStart=rootIndex+1, inEnd=inEnd)
        return root



if __name__ == '__main__':
    inOrder = [4, 10, 3, 1, 7, 11, 8, 2]
    preOrder = [7, 10, 4, 3, 1, 2, 8, 11]
    print 'inOrder:', str(inOrder)
    print 'preOrder:', str(preOrder)
    sol = Solution()
    sol.buildTree(preOrder=preOrder, inOrder=inOrder)