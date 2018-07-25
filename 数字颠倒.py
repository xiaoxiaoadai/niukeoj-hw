#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        num = input()
        res = num[::-1]
        print(''.join(res))
    except:
        break