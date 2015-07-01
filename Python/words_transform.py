__author__ = 'Han'

# transform one word to another by changing only 1 letter at a time
# we use a backtrack map if B[v] = w
# to reach our end word, we can use backtrack map to reverse our path

import string
import random


# construct a dictionary for testing purposes
letters = string.ascii_lowercase[:10]
dictionary = []
for i in range(1000):
    word = ''
    word += letters[random.randint(0, 9)]
    word += letters[random.randint(0, 9)]
    word += letters[random.randint(0, 9)]
    word += letters[random.randint(0, 9)]
    dictionary.append(word)



class Transform:
    def __init__(self, start, end):
        assert len(start) == len(end)
        self.start = start.lower()
        self.end = end.lower()
        self.action_queue = []
        self.visited_set = []
        self.backtrack = {}
        self.action_queue.append(self.start)
        self.visited_set.append(self.start)

    def do_transform(self):
        while self.action_queue != []:
            word = self.action_queue.pop(0)
            for v in self.get_one_edit_words(word):
                if v == self.end:
                    chain_list = []
                    chain_list.append(v)
                    while True:
                        chain_list.insert(0, word)
                        if self.backtrack.has_key(word):
                            word = self.backtrack[word]
                        else:
                            break
                    return chain_list
                else:
                    if v in dictionary:
                        if v not in self.visited_set:
                            self.action_queue.append(v)
                            self.visited_set.append(v)
                            self.backtrack[v] = word
        return None


    # return a list of strings containing all the potential new_words
    def get_one_edit_words(self, word):
        all_letters = string.ascii_lowercase
        words_list = []
        for i in range(len(word)):
            for c in all_letters:
                # if c is not the letter in position, we change it and store it
                if c != word[i]:
                    word_list = list(word)
                    word_list[i] = c
                    new_word = ''.join(word_list)
                    words_list.append(new_word)
        return words_list



if __name__ == '__main__':
    transform = Transform(dictionary[random.randint(0,999)], dictionary[random.randint(0, 999)])
    print 'start:', str(transform.start)
    print 'end:', str(transform.end)
    print transform.do_transform()



