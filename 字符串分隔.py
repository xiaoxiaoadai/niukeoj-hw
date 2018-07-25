#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        stringa = input()
        stringb = input()
        res = str()
        xa = str()
        xb = str()
        # 求余
        a = len(stringa) % 8
        if len(stringa) == 0 or a == 0:
            a = 0
        else:
            a = 8 - a
        xa = stringa + '0'*a

        b = len(stringb) % 8
        if len(stringb) == 0 or b == 0:
            b = 0
        else:
            b = 8 - b
        xb = stringb + '0'*b
        res = xa + xb
        #print('res=', res)
        for i in range(len(res)+1):
            if i % 8 == 0 and i != 0:
                print(res[i-8:i])
    except:
        break

