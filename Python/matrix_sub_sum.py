__author__ = 'Han'


import random


num_matrix = []
for i in xrange(5):
    sub_matrix = []
    for j in xrange(5):
        sub_matrix.append(random.randint(-10, 10))
    print(sub_matrix)
    num_matrix.append(sub_matrix)
print('')

class SubMatrix:
    def __init__(self, col, row, size):
        self.col = col
        self.row = row
        self.size = size

    def do_change(self, col=None, row=None, size=None):
        if col:
            self.col = col
        if row:
            self.row = row
        if size:
            self.size = size

    # [row][col], [row][col+size-1]
    # [row+size-1][col], [row+size-1][col+size-1]
    def do_sum(self):
        sub_sum = 0
        for row in xrange(self.size):
            for col in xrange(self.size):
                sub_sum += num_matrix[self.row+row][self.col+col]
        return sub_sum


# Brutal Force approach only sequentially checks every row and col
class Brutal_Force:
    def search(self):
        max_sum = 0
        final_sm = SubMatrix(0, 0, 0)
        for row in xrange(len(num_matrix)):
            for col in xrange(len(num_matrix)):
                size = len(num_matrix) - max(col, row)
                sm = SubMatrix(col, row, size)
                sm_sum = sm.do_sum()
                if sm_sum > max_sum:
                    final_sm.do_change(col, row, size)
                    max_sum = sm_sum
        return (final_sm, max_sum)


if __name__ == '__main__':
    bf = Brutal_Force()
    (final_sm, max_sum) = bf.search()
    print('row:', final_sm.row)
    print('col:', final_sm.col)
    print('size:', final_sm.size)
    print('sum:', max_sum)