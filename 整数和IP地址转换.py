#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ip_int(ip):
    """

    :param ip: IP 地址
    :return: 十进制IP
    """
    res = list()
    for i in ip:
        if int(i) not in range(0, 256) or len(ip) != 4:
            break
        else:
            res.append(bin(int(i)).lstrip('0b').rjust(8, '0'))
    if res != []:
        return int(''.join(res), base=2)
    else:
        return


def int_ip(inter):
    """

    :param inter: 整型字符串
    :return: IP
    """
    tmp = bin(int(inter)).lstrip('0b').rjust(32, '0')
    if tmp == '1'*32 or tmp == '0'*32:
        return
    a = tmp[:8]
    b = tmp[8:16]
    c = tmp[16:24]
    d = tmp[24:32]
    res2 = list()
    for k in a, b, c, d:
        if int(k, base=2) not in range(0, 256):
            return
        else:
            res2.append(str(int(k, base=2)))
    return '.'.join(res2)



while True:
    try:
        ip = input().split('.')
        inter = input()
        print(ip_int(ip))
        print(int_ip(inter))
    except:
        break