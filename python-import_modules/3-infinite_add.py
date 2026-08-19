#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    sum = 0
    for i in argv[1:]:
        sum += int(i)
    print(sum)
