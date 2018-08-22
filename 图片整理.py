#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        string = input()
        # FIXME:直接sorted（string)
        res = list(string)
        for i in range(len(res)):
            for j in range(i+1, len(res)):
                if res[i] > res[j]:
                    res[i], res[j] = res[j], res[i]
        print(''.join(res))
    except:
        break