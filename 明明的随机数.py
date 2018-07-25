#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        num = int(input())
        res = []
        for i in range(num):
            x = int(input())
            if x in res:
                continue
            res.append(x)
        res.sort()
        for i in res:
            print(i)
    except:
        break