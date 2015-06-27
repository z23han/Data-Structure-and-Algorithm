# only design algorithm printing out 3 digits at most
tens_list = {
    10: ' ten', 
    20: ' twenty',
    30: ' thirty',
    40: ' forty',
    50: ' fifty',
    60: ' sixty',
    70: ' seventy',
    80: ' eighty',
    90: ' ninety'
}

nums_list = {
    1: ' one',
    2: ' two',
    3: ' three',
    4: ' four',
    5: ' five',
    6: ' six',
    7: ' seven',
    8: ' eight',
    9: ' nine',
    10: ' ten',
    11: ' eleven',
    12: ' twelve',
    13: ' thirteen',
    14: ' fourteen',
    15: ' fifteen',
    16: ' sixteen',
    17: ' seventeen',
    18: ' eighteen',
    19: ' nineteen'
}

# dissect the number input n into smaller than 20 or
# bigger than 20 for the lower position digits
def convert2word(n):
    out_str = ''
    if n % 100 < 20:
        num = n % 100
        out_str = nums_list[num] + out_str
        left = n / 100
    else:
        num = n % 10
        out_str = nums_list[num] + out_str
        left = n / 10
        num = left % 10
        out_str = tens_list[num * 10] + out_str
        left = left / 10
    if left == 0:
        return out_str
    out_str = nums_list[num] + " hundred and"+ out_str
    return out_str

print convert2word(949)


num_tokens = {
    0: 'zero', 
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}


def int2word(n):
    num_list = reversed(print_dig(n))
    int_list = []
    for num in num_list:
        int_list.append(num_tokens[num])
    return int_list


def print_dig(n):
    dig_list = []
    left = n
    while True:
        if left == 0:
            break
        dig = left % 10
        left = left / 10
        dig_list.append(dig)
    return dig_list


