# adds 2 numbers not using + or any arithmetic operators

def add2nums(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    max_len = max(len(str1), len(str2))
    if len(str1) < max_len:
        str1 = '0'*(max_len - len(str1)) + str1
    if len(str2) < max_len:
        str2 = '0'*(max_len - len(str2)) + str2
    dig_lst = []
    for i in range(max_len):
        digit = int(str1[i]) ^ int(str2[i])
        dig_lst.append(digit)
    return dig_lst


print add2nums(18, 124)
