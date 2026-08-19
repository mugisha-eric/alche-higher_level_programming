#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique = []
    for i in range(len(my_list)):
        if my_list[i] not in unique:
            sum += my_list[i]
            unique.append(my_list[i])
    return sum
uniq_add([1,2,3,4,5,1])