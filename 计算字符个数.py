#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        inputs = input().split()
        string = inputs[0].lower()
        char = inputs[1].lower()
        print(string.count(char))
    except:
        break