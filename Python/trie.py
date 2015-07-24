__author__ = 'Han'

# implement a trie data structure

_end = '_end_'

def make_trie(*words):
    root = dict()
    for word in words:
        curr_dict = root
        for letter in word:
            curr_dict[letter] = {}
            curr_dict = curr_dict[letter]
            #curr_dict = curr_dict.setdefault(letter, {})
        curr_dict[_end] = _end
    return root

#print(make_trie('apple', 'banana', 'orange', 'pear'))

def in_trie(trie, word):
    curr_dict = trie
    for letter in word:
        if letter in curr_dict:
            curr_dict = curr_dict[letter]
        else:
            return False
    if _end in curr_dict:
        return True
    else:
        return False

#print(in_trie(make_trie('apple', 'banana', 'orange', 'pear'), 'apple'))


class Trie:
    def __init__(self):
        self.path = {}
        self.value = None
        self.value_valid = False

    def __setitem__(self, key, value):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.__setitem__(remains, value)
        else:
            node.value = value
            node.value_valid = True

    def __delitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
            if len(key) > 1:
                remains = key[1:]
                node.__delitem__(remains)
            else:
                node.value_valid = False
                node.value = None
            if len(node) == 0:
                del self.path[head]

    def __getitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            raise KeyError(key)
        if len(key) > 1:
            remains = key[1:]
            try:
                return node.__getitem__(remains)
            except KeyError:
                raise KeyError(key)
        elif node.value_valid:
            return node.value
        else:
            return KeyError(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
        except KeyError:
            raise KeyError(key)
        return True

    def __len__(self):
        if self.value_valid:
            n = 1
        else:
            n = 0
        for k in self.path.keys():
            n += len(self.path[k])
        return n

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def nodeCount(self):
        n = 0
        for k in self.path.keys():
            n = n + 1 + self.path[k].nodeCount()
        return n

    def __keys__(self, prefix=[], seen=[]):
        result = []
        if self.value_valid:
            isStr = True
            val = ""
            for k in seen:
                if type(k) != str or len(k) > 2:
                    isStr = False
                    break
                else:
                    val += k
            if isStr:
                result.append(val)
            else:
                result.append(prefix)
        if len(prefix) > 0:
            head = prefix[0]
            prefix = prefix[1:]
            if head in self.path:
                next_paths = [head]
            else:
                next_paths = []
        else:
            next_paths = self.path.keys()
        for k in next_paths:
            next_seen = []
            next_seen.extend(seen)
            next_seen.append(k)
            result.extend(self.path[k].__keys__(prefix, next_seen))
        return result

    def keys(self, prefix=[]):
        return self.__keys__(prefix)

    def __iter__(self):
        for k in self.keys():
            yield k
        raise StopIteration

    def __add__(self, other):
        result = Trie()
        result += self
        result += other
        return result

    def __sub__(self, other):
        result = Trie()
        result += self
        result -= other
        return result

    def __iadd__(self, other):
        for k in other:
            self[k] = other[k]
        return self

    def __isub__(self, other):
        for k in other:
            del self[k]
        return self


def assign(t, k, v):
    print("Assigning %s => t[%s]" % (v, k))
    t[k] = v


def dump(t):
    print("Dumping trie:")
    for k in t.keys():
        print(" t[%s] => %s" % (k, t[k]))


if __name__ == "__main__":
    print("\nUsing a simple string as keys and numeric values ...")
    t = Trie()
    assign(t, 'string1', 1)
    assign(t, 'string2', 2)
    dump(t)
    print('')
    print("\nUsing lists as keys and bool values ...")
    t1 = Trie()
    assign(t1, [1, 2], True)
    assign(t1, [2, 3], False)
    dump(t)
    print('')
    print("\nUsing mixed types as keys and values ...")
    t2 = Trie()
    assign(t2, [1, 2], 'Hello?')
    assign(t2, 'World', 'Earth')
    assign(t2, 'Planet Number', 3)
    assign(t2, (2, 1), 'X')
    dump(t2)



class Trie2:
    def __init__(self):
        self.children = {}
        self.value = None
        self.is_word = False

    def __add__(self, word):
        if len(word) == 0 or word == None:
            print("You have to add a real word")
            return
        self.value = word
        node = self
        for letter in word:
            if not node.children.has_key(letter):
                node.__put__(letter)
            node = node.children[letter]
        self.is_word = True

    def __put__(self, letter):
        node = Trie()
        node.__add__(self.children[letter])
        self.children[letter] = Trie()


    def contains(self, word):
        node = self
        for letter in word:
            if not node.children.has_key(letter):
                return False
            node = node.children[letter]
        print(node.children)
        return node.value == word

