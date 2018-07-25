#!/usr/bin/env python3
# -*- coding:ascii -*-

while True:
    try:
        chars = input()
        res = []
        for i in chars:
            if i in res:
                continue
            res.append(i)
        print(len(res))
    except:
        break