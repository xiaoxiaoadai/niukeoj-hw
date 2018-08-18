#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def compare2string(a, b):
    """
    compare between a and b
    :param a:
    :param b:
    :return: 1=(a>b);-1=(a<b);0=(a=b)
    """
    if a == b:
        return 0
    elif a in b:
        return 1
    elif b in a:
        return -1
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1


print(compare2string('abef', 'abc'))
