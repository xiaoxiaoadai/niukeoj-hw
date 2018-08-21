#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        strings = input()
        length = len(strings)
        if strings == strings[::-1]:
            print(len(strings))
            continue
        maxi = 0
        for i in range(length):
            # TODO: 分奇偶两种情况判断回文子序列
            if i - maxi == 0 and strings[i-maxi:i+maxi] == strings[i-maxi:i+maxi][::-1]:
                    maxi += 1
        print(maxi)
    except:
        break