#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ready(list_l):
    """
    获取所有符合条件的排列，并取最长的一种
    :param list_l: 数字列表
    :return: 最长的排列的长度
    """
    dict_i = dict()
    for i in range(len(list_l)):
        res_l = list()
        res_r = list()
        for j in range(len(list_l)):
            if i == j:
                continue
            # 左边的升序子序列
            if j < i:
                if list_l[i] > list_l[j]:
                    res_l.append(list_l[j])
            # 右边的降序子序列
            if j > i:
                if list_l[j] > list_l[i]:
                    res_r.append(list_l[j])
        # i 的左右子序列的长度之和
        dict_i[i] = len(res_l) + len(res_r) - 1
    # 求dict_i中value值最大的key
    return len(list_l)-max(dict_i.values()) + 1

while True:
    try:
        N = input()
        heights = input().split(' ')
        heights = [int(i) for i in heights]
        # TODO: 以每个点为顶点，求其左右的升序和降序子序列的最大的长度之和
        print(ready(heights))
    except:
        break