__author__ = 'Han'

# find the max sub-square with black color in a black and white square matrix

import random


def color_yield():
    if random.random() >= 0.5:
        return 'X'
    else:
        return '-'

color_matrix = []
for i in xrange(10):
    color_row = []
    for j in xrange(10):
        color_row.append(color_yield())
    color_matrix.append(color_row)


class Subsquare:
    def __init__(self, col, row, size):
        self.col = col
        self.row = row
        self.size = size

    def change(self, col=None, row=None, size=None):
        if col:
            self.col = col
        if row:
            self.row = row
        if size:
            self.size = size


class FindSquare:
    # this is more like expanding from the left to the right, easier to be visualized
    def find_out(self):
        current_max = 0
        sq = Subsquare(0, 0, 0)
        col = 0
        n = len(color_matrix)
        # check for col consecutively until arriving at the current_max
        while n - col > current_max:
            # for each col, check each row
            for row in xrange(len(color_matrix)):
                # get the size by excluding the max of row and col
                size = n - max(row, col)
                # intending to only check the possible bigger size, rather than smaller size
                while size > current_max:
                    # check if col & row & size can form a black square
                    if self.is_square(col, row, size):
                        # if successful, I need to update the current_max
                        current_max = size
                        # also update sq
                        sq.change(col, row, size)
                        break
                    size -= 1
            col += 1
        return sq

    # Used for checking the right and bottom forming a square with size
    def is_square(self, col, row, size):
        # we check horizontally
        for i in xrange(size):
            if color_matrix[row][col+i] == '-':
                return False
            if color_matrix[row+size-1][col+i] == '-':
                return False
        # we check vertically
        for i in xrange(size):
            if color_matrix[row+i][col] == '-':
                return False
            if color_matrix[row+i][col+size-1] == '-':
                return False
        # if all the checks have been examined, we pass
        return True


if __name__ == '__main__':
    for i in xrange(len(color_matrix)):
        print color_matrix[i]
    print ''
    find_sq = FindSquare()
    sq = find_sq.find_out()
    print('col:', sq.col)
    print('row:', sq.row)
    print('size:', sq.size)
