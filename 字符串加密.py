#!/usr/bin/env python3
# -*- coding:utf-8 -*-

alphabet = [chr(m) for m in range(65, 91)]

while True:
    try:
        key = input().upper()
        data = input().upper()
        # key先去重
        tmp = list()
        for i in key:
            if i not in tmp:
                tmp.append(i)
        key = tmp
        # 重构字母表alphabet2

        tmp2 = key + [j for j in alphabet if j not in key]
        alphabet2 = tmp2

        res = list()
        for k in data:
            res.append(alphabet2[alphabet.index(k)].lower())
        print(''.join(res))
    except:
        break