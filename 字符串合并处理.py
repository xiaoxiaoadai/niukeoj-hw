#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def my_sort(string):
    """
    x = 'dec'
    y = 'fab'
    print(my_sort(x+y))
    """
    temp = list(string)
    # TODO: 下标分别为奇偶的两个子序列分别形成有序
    for i in range(len(string)):
        for j in range(i+2, len(string), 2):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
    return ''.join(temp)


def my_trans(char):
    # TODO: 把0-9和a-f和A-F的字符进行转换


