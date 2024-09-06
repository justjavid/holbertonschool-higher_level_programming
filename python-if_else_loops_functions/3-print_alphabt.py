#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) in ("q", "e"):
        continue
    print("{}".format(chr(x)), end="")
