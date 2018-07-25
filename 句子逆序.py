#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        strings = input().split()
        print(' '.join(strings[::-1]))
    except:
        break