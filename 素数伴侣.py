#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def is_prime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            # print(i)
            return False
    return True

while True:
    try:
        n = input()
        ints = input().split()
        # TODO: 素数和一定是奇数和偶数相加的结果，先把输入的数分成奇偶两部分，然后再用匈牙利算法
    except:
        break