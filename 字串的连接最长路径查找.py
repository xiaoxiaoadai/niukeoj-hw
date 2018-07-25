#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def compare(a, b):
    """
    输入两个字符串，根据字典序列排序
    :param a:字符串a
    :param b:字符串b
    :return: a >= b则返回1，否则返回-1
    """
    if len(a) == 1 or len(b) == 1:
        if a[0] > b[0]:
            return 1
        elif a[0] < b[0]:
            return -1
        else:
            if len(a) == 1:
                return -1
            else:
                return 1
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
        if i == min(len(a), len(b)) - 1:
            if a[i] is not None:
                return 1
            else:
                return -1



while True:
    try:
        res = list()
        num = int(input())
        for i in range(num):
            string = input()
            res.append(string)
        for i in sorted(res):
            print(i)
    except:
        break
