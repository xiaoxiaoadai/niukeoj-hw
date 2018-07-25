#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def extract(num):
    """
    从range(2, num+1)中取整数作为因子来尝试被num整除
    :param num:
    :return:
    """
    if num < 2:
        return [num]
    res = num
    res_list = list()
    while True:
        try:
            for i in range(2, num+1):
                if res % i == 0:
                    # print("before:", res)
                    res = res // i
                    # print("after:", res)
                    # print("i:", i)
                    res_list.append(i)
                    break
            if res == 1:
                break
        except:
            break
    return res_list


while True:
    try:
        num = int(input())
        reslist = [str(i) for i in extract(num)]
        # 注意输出格式的要求
        print(' '.join(reslist)+' ')
    except:
        break