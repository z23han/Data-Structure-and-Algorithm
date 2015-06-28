# randomly generate a set of m integers from an array with equal prob

import random

def gen_m_int(lst):
    m = int(random.random() * len(lst))
    out_len = m
    for i in range(len(lst)):
        index = int(random.random()*(len(lst) - i)) + i
        temp = lst[index]
        lst[index] = lst[i]
        lst[i] = temp
        m -= 1
        if m == 0:
            break
    return lst[:out_len]

set_array = list(range(20))
print gen_m_int(set_array)
