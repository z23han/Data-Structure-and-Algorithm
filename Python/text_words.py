# -*- coding: cp936 -*-
import re, collections

class TextWords(object):
    def __init__(self, text):
        self.text = text

    def get_words(self):
        return re.sub(r'[^a-z0-9]', ' ', self.text.lower()).split()

    def create_index(self):
        index = collections.defaultdict(list)
        words = self.get_words()
        for pos, word in enumerate(words):
            index[word].append(pos)
        return index
    
    def query_index(self, index, word):
        if word in index:
            return index[word]
        else:
            return []


class Node:
    # use Hashtable to store children
    # use isTerminal to indicate the end leaf of the branch
    def __init__(self, letter=None, isTerminal=False):
        self.letter = letter
        self.children = {}
        self.isTerminal = isTerminal
        self.positions = []




class Trie:
    def __init__(self):
        self.root = Node('')

    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            # get the current children letter, and update current
            current = current.children[letter]
        return current.isTerminal

    def __getitem__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True
        return current.positions

    def __str__(self):
        self.output([self.root])
        return ''

    def output(self, currentPath, indent=''):
        currentNode = currentPath[-1]
        if currentNode.isTerminal:
            word = ''.join([node.letter for node in currentPath])
            print indent+word+' '+str(currentNode.positions)
            indent += '  '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:]+[node], indent)


def get_words(self):
    return re.sub(r'[^a-z0-9]', ' ', self.text.lower()).split()

def create_index(text):
    trie = Trie()
    words = get_words(text)
    for pos, word in enumerate(words):
        trie[word].append(pos)
    return trie

def query_index(index, word):
    if word in index:
        return index[word]
    else:
        return []




if __name__ == '__main__':
    text = '''Once we build the index we can answer any query.
        Given a word, just return its position array if it
        exists in the hashtable index. Otherwise, if the word
        isn’t present in the index, it means that the word
        doesn’t appear in the file, so return an empty list.'''
    #text_words = TextWords(text)
    #index = text_words.create_index()
    #whattt = text_words.query_index(index, 'index')
    #print whattt

    
        
