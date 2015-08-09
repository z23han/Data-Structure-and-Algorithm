__author__ = 'ZHIXU'

# Given 2 binary trees, check if they are equal or not
# 2 Binary trees are equal if they are structurally identical and nodes have the same value

import random

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = None

    def __insert__(self, val):
        if self.head == None:
            self.head = TreeNode(val)
            return
        curr = self.head
        prev = None
        while curr != None:
            prev = curr
            if val <= curr.val:
                curr = curr.left
            else:
                curr = curr.right
        newNode = TreeNode(val)
        if val <= prev.val:
            prev.left = newNode
        else:
            prev.right = newNode
        return

    def __search__(self, node, val):
        if node == None or val == node.val:
            return node
        if val < node.val:
            return self.__search__(node.left, val)
        else:
            return self.__search__(node.right, val)

    def __minimum__(self):
        if self.head == None:
            return None
        curr = self.head
        while curr.left != None:
            curr = curr.left
        return curr.val

    def __maximum__(self):
        if self.head == None:
            return None
        curr = self.head
        while curr.right != None:
            curr = curr.right
        return curr.val

    def __inOrderWalk__(self, node):
        if node != None:
            self.__inOrderWalk__(node.left)
            print node.val
            self.__inOrderWalk__(node.right)
        return

    def __preOrderWalk__(self, node):
        if node != None:
            print node.val
            self.__preOrderWalk__(node.left)
            self.__preOrderWalk__(node.right)
        return

    def __postOrderWalk__(self, node):
        if node != None:
            self.__preOrderWalk__(node.left)
            self.__preOrderWalk__(node.right)
            print node.val
        return

    def __delete__(self, val):
        pass


class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p != None and q != None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    bt1 = BinaryTree()
    bt2 = BinaryTree()
    for i in xrange(10):
        num = random.randint(1, 20)
        bt1.__insert__(num)
        bt2.__insert__(num)
    sol = Solution()
    print sol.isSameTree(bt1.head, bt2.head)