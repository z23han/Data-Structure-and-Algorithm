# find all pairs of integers within an array summing to a value
# for example: {-2 -1 0 3 5 6 7 9 13 14 }

lst = [-2, -1, 0, 3, 5, 6, 7, 9, 13, 14]
total = 12

def print_pairs(lst, total):
    in_lst = sorted(lst)
    out_lst = []
    first = 0
    last = len(in_lst) - 1
    while first < last:
        s = in_lst[first] + in_lst[last]
        if s == total:
            out_lst.append((in_lst[first], in_lst[last]))
            first += 1
            last -= 1
        else:
            if s < total:
                first += 1
            else:
                last -= 1
    return out_lst


def find_pairs(lst, total):
    out_lst = []
    in_lst = list(lst)
    while in_lst != []:
        one = in_lst.pop(0)
        another = total - one
        #print another
        if in_lst != []:
            for ele in in_lst:
                if ele == another:
                    out_lst.append((one, another))
                    in_lst.pop(in_lst.index(ele))
                    break
        else:
            break
    return out_lst


print find_pairs(lst, total)
print print_pairs(lst, total)
