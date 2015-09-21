__author__ = 'ZHIXU'

# Listing and labeling all of the permutations in order,
# and return the kth permutation sequence

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        pass

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n*self.factorial(n-1)

    def allPermutations(self, numList, low=0):
        if low + 1 >= len(numList):
            yield numList
        else:
            for p in self.allPermutations(numList, low+1):
                yield p
            for i in xrange(low+1, len(numList)):
                numList[low], numList[i] = numList[i], numList[low]
                for p in self.allPermutations(numList, low+1):
                    yield p
                numList[low], numList[i] = numList[i], numList[low]


if __name__ == '__main__':
    sol = Solution()
    for p in sol.allPermutations([1,2,3,4]):
        print(p)