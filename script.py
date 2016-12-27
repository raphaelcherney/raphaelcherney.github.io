# script that outputs a string of random numbers (to be used to name pictures)

import random

def make_number(length):
    number = ''
    for i in range(length):
        number += str(random.randint(0,9))
    return number

def make_number_list(filename, count, length):
    f = open(filename, 'w')
    for i in range(count):
        f.write(make_number(length) + '\n')
    f.close()

make_number_list('numbers.txt', 200, 5)
print 'Done.'