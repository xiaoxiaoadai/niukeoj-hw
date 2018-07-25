#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        num = int(input())
        num_bin = bin(num)
        count_1 = str(num_bin).count('1')
        print(count_1)
    except:
        break