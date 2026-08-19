#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    filetered = sorted([nice for nice in names if not nice.startswith("__")])
    for name in filetered:
        print(name)
