#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def josephus(n, k):
    link = list(range(n))
    # link = [0, 1, 2, 3, 4 ..., n-1]
    index = 0
    for i in range(n-1):
        # i in [0, 1, 2, 3, 4 ... n-2]
        index = (index + k) % len(link)
        # index -= 1
        print('KILLED: ', link[index], len(link))
        del link[index]

    print('RESULT: ', link[0])


def myjosephus(n):
    """
    :param n: 人数n
    :return: 最后一个数
    """
    # 每隔两个数删一个，即三个数里删一个
    m = 3
    if n == 1:
        return 0
    return (myjosephus(n-1)+m) % n

n = int(input())
josephus(n, k=2)
print('myjosephus: ', myjosephus(n))
