#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        top = 0
        dem = 0
        for tup in my_list:
            top += (tup[0] * tup[1])
            dem += tup[1]
        return (top / dem)
    return 0
