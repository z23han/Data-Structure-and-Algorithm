__author__ = 'Han'

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.value = None
        self.indexes = []

    def __insert__(self, string, index):
        self.indexes.append(index)
        if string != '' and len(string) > 0:
            self.value = string[0]
            child = SuffixTreeNode()
            if self.children.has_key(self.value):
                child = self.children[self.value]
            else:
                self.children[self.value] = child
            remainder = str(string[1:])
            child.__insert__(remainder, index)

    def __getIndexes__(self, string):
        if string == '' or len(string) == 0:
            return self.indexes
        else:
            first = string[0]
            if self.children.has_key(first):
                remainder = str(string[1:])
                return self.children[first].__getIndexes__(remainder)
        return None


class SuffixTree:
    def __init__(self, string):
        self.root = SuffixTreeNode()
        for i in range(len(string)):
            suffix = str(string[i:])
            self.root.__insert__(suffix, i)

    def __getIndexes__(self, string):
        return self.root.__getIndexes__(string)


if __name__ == '__main__':
    test_str = 'mississippi'
    str_list = ['is', 'sip', 'hi', 'sis']
    tree = SuffixTree(test_str)
    for s in str_list:
        index_list = tree.__getIndexes__(s)
        if index_list != None:
            print s + ": " + str(index_list)



