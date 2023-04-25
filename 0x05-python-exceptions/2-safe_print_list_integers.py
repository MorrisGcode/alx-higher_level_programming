#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num_printed)
