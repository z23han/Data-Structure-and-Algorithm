__author__ = 'ZHIXU'

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

import random

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = ListNode(val)
        else:
            curNode = self.root
            nextNode = self.root.next
            while nextNode != None:
                curNode = nextNode
                nextNode = curNode.next
            curNode.next = ListNode(val)
        return


class oneLinkedList:
    def __init__(self):
        self.ll = None

    def generateList(self, n):
        nVal = [random.randint(1, 100) for _ in xrange(n)]
        self.ll = LinkedList()
        for val in nVal:
            self.ll.add(val)
        return self.ll

    def printList(self):
        node = self.ll.root
        valList = []
        while node != None:
            valList.append(node.val)
            node = node.next
        return valList


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pass


if __name__ == '__main__':
    ll = oneLinkedList()
    ll.generateList(10)
    print ll.printList()