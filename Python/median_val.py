__author__ = 'Han'

import random

class Median_val:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert(self, val):
        max_len = len(self.max_heap)
        min_len = len(self.min_heap)
        # if max_heap is empty
        if max_len == 0:
            self.max_heap.append(val)
            return
        # if min_heap is empty
        if min_len == 0:
            if self.max_heap[0] >= val:
                self.min_heap.append(val)
                return
            else:
                self.min_heap.append(self.max_heap.pop(0))
                self.max_heap.append(val)
                return
        # compare val with max_heap[max_len-1]
        if val >= self.max_heap[max_len-1]:
            if max_len <= min_len:
                for i in range(max_len):
                    if val >= self.max_heap[i]:
                        self.max_heap.insert(i, val)
                        return
            else:
                self.min_heap.append(self.max_heap.pop(max_len-1))
                for i in range(max_len-1):
                    if val >= self.max_heap[i]:
                        self.max_heap.insert(i, val)
                        return
                self.max_heap.append(val)
                return
        # compare val with min_heap[min_len-1]
        elif val <= self.min_heap[min_len-1]:
            if min_len <= max_len:
                for i in range(min_len):
                    if val <= self.min_heap[i]:
                        self.min_heap.insert(i, val)
                        return
            else:
                self.max_heap.append(self.min_heap.pop(min_len-1))
                for i in range(min_len-1):
                    if val <= self.min_heap[i]:
                        self.min_heap.insert(i, val)
                        return
                self.min_heap.append(val)
                return
        # if val is exactly in the middle of the extreme cases
        else:
            if max_len <= min_len:
                self.max_heap.append(val)
                return
            else:
                self.min_heap.append(val)
                return

    def get_median(self):
        max_len = len(self.max_heap)
        min_len = len(self.min_heap)
        if max_len == 0 and min_len == 0:
            return None
        if max_len == min_len:
            return (0.5 * (self.max_heap[max_len-1] + self.min_heap[min_len-1]))
        elif max_len > min_len:
            return self.max_heap[max_len-1]
        else:
            return self.min_heap[min_len-1]

    def get_max_heap(self):
        return self.max_heap

    def get_min_heap(self):
        return self.min_heap



def rand100():
    for i in xrange(10):
        yield random.randrange(1, 199)

if __name__ == "__main__":
    median_val = Median_val()
    rand_lst = []
    for item in rand100():
        rand_lst.append(item)
        print 'item:', str(item)
        median_val.insert(item)
        print rand_lst
        print 'max_heap:', str(median_val.get_max_heap())
        print 'min_heap:', str(median_val.get_min_heap())
        print 'median value: ', str(median_val.get_median())
        print ''

