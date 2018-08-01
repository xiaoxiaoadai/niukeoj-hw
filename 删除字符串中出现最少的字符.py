#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        string = input()
        res = dict()
        res_l = list()
        for i in string:
            if i in res.keys():
                res[i] += 1
                res_l.append(i)
            else:
                res[i] = 1
                res_l.append(i)
        mix = min(res.values())
        for j in res.keys():
            if res[j] == mix:
                for k in range(mix):
                    res_l.remove(j)

        print(''.join(res_l))
    except :
        break