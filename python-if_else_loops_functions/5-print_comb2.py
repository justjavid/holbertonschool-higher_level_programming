#!/usr/bin/python3
for x in range(100):
    if x == 99:
        print ("{:2d}".format(x))
        break
    print("{:2d}, ".format(x), end="")
