__author__ = 'ZHIXU'
'''
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        toFind = dict()
        found = dict()
        result = []
        m = len(words)
        n = len(words[0])
        for word in words:
            if word not in toFind:
                toFind[word] = 1
            else:
                toFind[word] += 1

        for i in range(len(s)-m*n+1):
            found = {}
            j = 0
            for j in range(m):
                k = i + j * n
                stub = s[k:k+n]
                if stub not in toFind:
                    j -= 1
                    break
                if stub not in found:
                    found[stub] = 1
                else:
                    found[stub] += 1
                if found[stub] > toFind[stub]:
                    j -= 1
                    break
            if j == m-1:
                print(found)
                result.append(i)
        return result


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words=  ["foo", "bar"]
    sol = Solution()
    print sol.findSubstring(s, words)