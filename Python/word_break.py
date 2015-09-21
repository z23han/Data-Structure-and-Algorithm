__author__ = 'ZHIXU'

# Given a string s and a dictionary of words dict, determine if s can be
# segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

dictionary = ["leet", "code", "programcree", "program", "creek"]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        return self.wordBreakHelper(s, wordDict, 0)

    # the naive search algorithm simply checks every element in the wordDict
    def wordBreakHelper(self, s, wordDict, start):
        if start == len(s):
            return True

        for key in wordDict:
            wordLen = len(key)
            end = start + wordLen

            if end > len(s):
                continue
            if s[start:end] == key:
                if self.wordBreakHelper(s, wordDict, end):
                    return True
        return False

    def word_break2(self, s, wordDict):
        t = []
        t.append(True)

        for i in xrange(len(s)):
            if not t[i]:
                continue

            for key in wordDict:
                wordLen = len(key)
                end = i + wordLen
                if end > len(s):
                    continue
                if t[end]:
                    continue
                if s[i:end] == key:
                    t[end] = True

        return t[len(s)]


if __name__ == '__main__':
    sol = Solution()
    myStr = 'programcreek'
    print sol.wordBreak(myStr, dictionary)
