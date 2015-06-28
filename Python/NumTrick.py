# class wrapping all the possible methods manipulating numbers

import math
import random

class NumTrick(object):
    def __init__(self, lst):
        self.lst = lst

    # count the number of Ks in a set of number array
    # convert all int into string and evaluate
    def countKs(self, K):
        assert K >= 0 and K <= 9
        in_lst = []
        for num in self.lst:
            in_lst.append(str(num))
        strK = str(K)
        cnt = 0
        for ele in in_lst:
            for dig in ele:
                if dig == strK:
                    cnt += 1
        return cnt

    # the pattern is that
    # 1 K in every 10, 10 K in every 100, 100 K in every 1000
    # ERROR !!!
    def countKs2(self, K):
        assert K >= 0 and K <= 9
        lst_len = len(self.lst)
        cnt = 0
        if lst_len > 9:
            cnt += lst_len / 10
            rem = lst_len % 10
            print '10:', str(rem)
            if rem-1 >= K:
                cnt += 1
        if lst_len > 99:
            cnt += lst_len / 100 * 10
            rem = lst_len % 100
            print '100:', str(rem)
            if rem-1 >= 10*(K+1):
                cnt += 10
            elif rem-1 >= 10*K:
                cnt += rem - 10*K + 1
        if lst_len > 999:
            cnt += lst_len / 1000 * 100
            rem = lst_len % 1000
            print '1000:', str(rem)
            if rem-1 >= 100*(K+1):
                cnt += 100
            elif rem-1 >= 100*K:
                cnt += rem - 100*K + 1
        if lst_len > 9999:
            cnt += lst_len / 10000 * 1000
            rem = lst_len % 10000
            print '10000:', str(rem)
            if rem-1 >= 1000*(K+1):
                cnt += 1000
            elif rem-1 >= 1000*K:
                cnt += rem - 1000*K + 1
        return cnt

    def count2sR(self, n):
        if n == 0:
            return 0
        power = 1
        while 10*power < n:
            power *= 10
        first = n / power
        remainder = n % power
        n2sFirst= 0
        if first > 2:
            n2sFirst += power
        elif first == 2:
            n2sFirst += remainder + 1
        n2sOther = first * self.count2sR(power-1) + self.count2sR(remainder)
        return n2sFirst + n2sOther

    def count2sI(self, n):
        countof2s = 0
        digit = 0
        j = n
        seendigits = 0
        position = 0
        pow10_pos = 1
        while j > 0:
            digit = j % 10
            pow10_posMinus1 = pow10_pos / 10
            countof2s += digit * position * pow10_posMinus1
            if digit == 2:
                countof2s += seendigits + 1
            elif digit > 2:
                countof2s += pow10_pos
            seendigits = seendigits + pow10_pos * digit
            pow10_pos *= 10
            position += 1
            j = j / 10
        return countof2s
    

# class wrapping string manipulations
class StrTrick(object):
    def __init__(self, str_in):
        self.str_in = str_in
        self.lst = str_in.split()

    def shortest_dist_words(self, word1, word2):
        dist1_lst = []
        dist2_lst = []
        cnt = 0
        for ele in self.lst:
            cnt += 1
            if ele == word1:
                dist1_lst.append(cnt)
            elif ele == word2:
                dist2_lst.append(cnt)
        # create a dictionary to hold the pairs
        dist_dict = {}
        for v1 in dist1_lst:
            for v2 in dist2_lst:
                v = abs(v1 - v2)
                dist_dict[v] = (v1, v2)
        total_dist = dist_dict.keys()
        v = sorted(total_dist)[0]
        return [v, dist_dict[v]]
    


if __name__ == '__main__':
    K = 1
    lst = list(range(56))
    num_trick = NumTrick(lst)
    str_in = '''Use two loops: The outer loop picks all the elements
    of arr[] one by one. The inner loop picks all the elements after
    the element picked by outer loop. If the elements picked by outer
    and inner loops have same values as x or y then if needed update
    the minimum distance calculated so far.Use two loops: The outer
    loop picks all the elements of arr[] one by one. The inner loop
    picks all the elements after the element picked by outer loop.
    If the elements picked by outer and inner loops have same values
    as x or y then if needed update the minimum distance calculated
    so far.'''
    word1 = 'inner'
    word2 = 'outer'
    str_trick = StrTrick(str_in)
    print str_trick.shortest_dist_words(word1, word2)

    
