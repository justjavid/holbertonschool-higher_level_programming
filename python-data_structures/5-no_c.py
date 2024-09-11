#!/usr/bin/python3
def no_c(my_string):
    a = list(my_string)
    for i in a:
        if i == 'c' or i == 'C':
            a.remove(i)
    my_string = "".join(a)
    return my_string
