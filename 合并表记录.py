#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        num = int(input())
        res = dict()
        for i in range(num):
            dict_input = input().split()
            if int(dict_input[0]) in res:
                res[int(dict_input[0])] += int(dict_input[1])
            else:
                res[int(dict_input[0])] = int(dict_input[1])
        res_list = sorted(res, reverse=False)
        # print(res_list) /* 注意及时注释掉多余的print */
        for i in res_list:
            print(i, res[int(i)])
    except:
        break