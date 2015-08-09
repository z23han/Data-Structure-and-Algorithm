__author__ = 'ZHIXU'

# Given a linked list, swap every two adjacent nodes and return its head.

import random

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def __insert__(self, val):
        if self.head == None:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = ListNode(val)
        return

    def __delete__(self, val):
        if self.head == None:
            return
        if self.head.val == val:
            if self.head.next == None:
                self.head = None
                return
            else:
                self.head = self.head.next
                return
        curr = self.head
        next = self.head.next
        while next != None:
            if next.val == val:
                curr.next = next.next
                return
            else:
                curr = next
                next = curr.next
        print("No such a value!")
        return

    def __print__(self):
        if self.head == None:
            return
        curr = self.head
        lst = []
        while curr != None:
            lst.append(curr.val)
            curr = curr.next
        print lst
        return


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head == None:
            return
        if head.next == None:
            return head
        curr = head
        next = curr.next
        new_head = next
        pt = new_head
        pt.next = curr
        pt = pt.next
        while True:
            curr = next.next
            if curr == None:
                break
            next = curr.next
            if next == None:
                pt.next = curr
                pt = pt.next
                break
            pt.next = next
            pt = pt.next
            pt.next = curr
            pt = pt.next
        pt.next = None
        return new_head


if __name__ == '__main__':
    ll = LinkedList()
    for i in xrange(10):
        ll.__insert__(random.randint(1, 20))
    ll.__print__()
    val = random.randint(1, 20)
    print(val)
    ll.__delete__(val)
    ll.__print__()
    sol = Solution()
    print sol.swapPairs(ll.head).val

