__author__ = 'Han'

# arranging 3 letter words in a 2d matrix, such that each row, col,
# and diagonal forms a word

class Arrange_words:
    def __init__(self):
        self.singleL = {}
        self.doubleL = {}

    # 1). singleL used for storing word (X1, X2, X3)
    # 2). doubleL used for storing word (Y1, Y2, Y3), such that we have the strings
    # that [X1, Y1], [X2, Y2], [X3, Y3], [X1, Y2], [X3, Y2] covered
    # in the dictionary.
    # 3). Lastly choose the third word Z from dictionary, thus we have
    # [X1, Y1, Z1], [X2, Y2, Z2], [X3, Y3, Z3], [X1, Y2, Z3], [X3, Y2, Z1],
    # otherwise go back to step 2

    def arrange(self, words_list):
        if len(words_list) == 0:
            return False
        # I store the first letter in the singleL
