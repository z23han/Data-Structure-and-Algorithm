# given an array of integers, find the continuous sequence
# with the largest sum
# input: {2, -8, 3, -2, 4, -10}
# output: 5 ({3, -2, 4})

def find_cont_sum(lst):
    current_sum = 0
    current_max = 0
    current_bucket = []
    max_bucket = []
    for i in range(len(lst)):
        current_sum += lst[i]
        current_bucket.append(lst[i])
        if current_max < current_sum:
            current_max = current_sum
            # should clone it rather than directly assign the list
            max_bucket = list(current_bucket)
        elif current_sum < 0:
            current_sum = 0
            current_bucket = []
    return (current_max, max_bucket)

input_lst = [2, -8, 3, -2, 4, -10]
print find_cont_sum(input_lst)

