#!/usr/bin/python3
def uppercase(str):
    final = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            final += chr(ord(char) - 32)
        else:
            final += char
    print("{}".format(final))
