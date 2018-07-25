#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 小数点后的数的第一个数字，四舍五入
while True:
    try:
        string = input()
        # print("string:", string)
        mylist = string.split(".")
        # print('mylist:', mylist)
        if int(mylist[1][0]) >= 5:
            print(int(mylist[0]) + 1)
        else:
            print(int(mylist[0]))
    except:
        break