__author__ = 'ZHIXU'

'''
Given a string s and a dictionary of words dict, add spaces in s to construct
a sentence where each word is a valid dictionary word.
Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s:
            return []

        n = len(s)
        dp = [[] for x in range(n+1)]
        dp[0] = [0]

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i].append(j)

        res = []
        self.backTracking(dp, s, n, res, '')
        return res

    def backTracking(self, dp, s, idx, res, line):
        for i in dp[idx]:
            newLine = s[i:idx] + ' ' + line if line else s[i:idx]

            if i == 0:
                res.append(newLine)
            else:
                self.backTracking(dp, s, i, res, newLine)


if __name__ == '__main__':
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    sol = Solution()
    res = sol.wordBreak(s, dict)
    print res