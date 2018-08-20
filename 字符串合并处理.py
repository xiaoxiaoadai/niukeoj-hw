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
    '''
    >>> my_trans('1')
    '8'
    '''
    # TODO: 把0-9和a-f和A-F的字符进行转换
    dic = '0123456789abcdef'
    if ord('0') <= ord(char) <= ord('9') or ord('a') <= ord(char.lower()) <= ord('f'):
        # 直接切片倒序
        index = bin(dic.index(char.lower())).lstrip('0b')
        index = '0'*(4-len(index)) + index
        index = index[::-1]
        # 将倒序后的二进制转十进制
        index = int(index, base=2)
        return dic[index].upper()
    else:
        return char


while True:
    try:
        str1, str2 = input().split()
        # str2 = input()
        strings = str1 + str2
        strings = my_sort(strings)
        res = list()
        for i in strings:
            res.append(my_trans(i))
        print(''.join(res))
    except:
        break