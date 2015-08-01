# rotate a list right by k places.

import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(random.randint(1, 100))
        self.length = 0

    def myList(self, length):
        self.length = length
        next = self.head
        for i in xrange(self.length-1):
            new = ListNode(random.randint(1, 100))
            next.next = new
            next = new
        return self.head

    def printList(self):
        l = []
        node = self.head
        for i in xrange(self.length):
            l.append(node.val)
            node = node.next
        print(l)


class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        assert isinstance(head, ListNode), "head should be a ListNode"
        assert k >= 0, "k should be non-negative"
        if k == 0:
            return head
        curr = head
        next = head.next
        new_head = None
        cnt = 0
        while next != None:
            cnt += 1
            if cnt == k:
                new_head = next
                curr.next = None
                curr = new_head
                next = curr.next
            else:
                curr = next
                next = curr.next
        curr.next = head
        return new_head


def printLinkedList(head):
    if head == None:
        return None
    l = []
    while head != None:
        l.append(head.val)
        head = head.next
    return l



if __name__ == '__main__':
    aList = LinkedList()
    head = aList.myList(10)
    aList.printList()
    sol = Solution()
    new_head = sol.rotateRight(head, 7)
    print printLinkedList(new_head)
