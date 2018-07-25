#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        num = input()
        res = []
        for i in num[::-1]:
            if i in res:
                continue
            res.append(i)
        print(''.join(res))
    except:
        break