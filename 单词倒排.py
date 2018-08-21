#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        strings = input()
        tmp = list(strings)
        for i in range(len(tmp)):
            if not tmp[i].isalpha():
                tmp[i] = ' '
        strings = ''.join(tmp).strip(' ').split()
        print(' '.join(strings[::-1]))
    except:
        break