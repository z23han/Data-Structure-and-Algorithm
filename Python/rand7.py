# generate a random number between 1 and 7, given a method
# that generates a random number between 1 and 5

import random

def rand5():
    return random.randint(1, 5)

# generate [1-7]
def rand7():
    num = 5* (rand5()-1)
    return (num % 7 + 1)


for i in range(5):
    print rand7()
