#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def get_sublist(num1, mylist1):
    """
    mylist = [1 ,2, 3, 4, num]
    :param num1:
    :return: 一个蛇形矩阵的第一行
    """
    # mylist = list(range(1, num1 + 1))
    res1 = list()
    idx = 0
    i = 0
    while idx < len(mylist1):
        res1.append(mylist1[idx])
        idx += (i+2)
        i += 1
    return res1


# mylist = list(range(1, 11))
# print(get_sublist(4, mylist))


while True:
    try:
        num = int(input())
        if num == 0:
            continue
        # 第一行从1到(num * (num+1)) //  2
        # (num * (num+1)) // 2也是矩阵中最大的数
        maxi = num * (num+1) // 2
        my_list = list(range(1, maxi+1))
        tmp = list()
        for i in range(num):
            tmp = get_sublist(num-i, my_list)
            # print(tmp)
            # 核心思路就是一行一行打印蛇形矩阵
            print(' '.join([str(j) for j in tmp]))
            # 更新my_list，将已经打印出来的数剔除
            my_list = [k for k in my_list if k not in tmp]
    except:
        break
