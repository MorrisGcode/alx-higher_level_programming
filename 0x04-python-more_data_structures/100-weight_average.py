#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    num = 0
    den = 0

    for i in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
