#!/usr/bin/python3
def islower(c):
    if ord('z') >= ord(c) >= ord('a'):
        return True
    else:
        return False


def uppercase(str):
    new_word = ""
    for x in str:
        if islower(x) is True:
            x = chr(ord(x) - 32)
        new_word += x
    print("{}".format(new_word))
