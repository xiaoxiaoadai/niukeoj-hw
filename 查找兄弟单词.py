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


def bubblesort(strings):
    """
    bubble sort a string list
    :param strings:
    :return:
    """
    length = len(strings)
    if length <= 1:
        return strings
    # res = list()
    res = strings
    for i in range(length):
        for j in range(i+1, length):
            if compare2string(strings[i], strings[j]) == 1:
                res[i], res[j] = res[j], res[i]
    return res


while True:
    try:
        strings = input().split()
        n = strings[1]
        # n = input()
        string_dict = strings[2:-2]
        # 排序后的字典
        # FIXME: 字典去重？
        string_dict = bubblesort(string_dict)
        # key = strings[-1]
        # 匹配关键字兄弟
        keys = strings[-2]
        # strings = strings[:-1]
        # 输出第m个兄弟单词
        m = int(strings[-1])
        res = list()
        count = 0
        for i in string_dict:
            if keys == i:
                continue
            if sorted(list(keys)) == sorted(list(i)):
                count += 1
                #if i not in res:
                res.append(i)
        res = bubblesort(res)
        # print("{0} {1} ".format(count, res[m-1]))

        print(count)
        if len(res) < m:
            # print(0)
            continue
        print(res[m-1])
    except:
        break
