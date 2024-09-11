#!/usr/bin/python3
def no_c(my_string):
    a = list(my_string)
    for i in range(len(a)):
        if a[i] == 'c' or a[i] == 'C':
            a.remove(a[i])
    my_string = "".join(a)
    return my_string
