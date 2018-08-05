#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        # 根据字母表顺序给输入的字符串中的字符排序
        strings = input()
        strings = list(strings)
        # alphabet = [chr(n) for n in range(97, 123)]
        res = list()

        length = len(strings)
        for i in range(length):
            if not strings[i].isalpha():
                continue
            for j in range(length):
                if not strings[j].isalpha():
                    continue
                if strings[i].lower() > strings[j].lower():
                    strings[i], strings[j] = strings[j], strings[i]
                # TODO: 解决大小写字符按原始顺序排序的问题
                elif (strings[i].isupper() and strings[j].islower()) or (strings[i].islower() and strings[j].isupper()):


        print(''.join(strings))
    except:
        break