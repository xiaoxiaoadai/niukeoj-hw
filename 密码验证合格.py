#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        string = input()
        if len(string) <= 8:
            print('NG')
            continue
        # 0~9
        a = 0
        # A~Z
        b = 0
        # a~z
        c = 0
        # 其他
        d = 0
        for i in string:
            if ord('0') <= ord(i) <= ord('9'):
                a = 1
            elif ord('A') <= ord(i) <= ord('Z'):
                b = 1
            elif ord('a') <= ord(i) <= ord('z'):
                c = 1
            # 其实这里分四个类别主要就是为了要求密码字符串至少有三类字符
            else:
                d = 1
        if a + b + c + d < 3:
            print('NG')
            continue
        tmp = 0
        for j in range(len(string) - 1):
            if string[j:j+3] in string[j+3:]:
                print('NG')
                tmp = 1
                break
        if tmp != 1:
            print('OK')
    except:
        break