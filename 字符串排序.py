#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        # 根据字母表顺序给输入的字符串中的字符排序
        strings = input()
        # strings = list(strings)
        # pure_string 是纯字母字符列表
        pure_strings = [i for i in strings if i.isalpha()]
        alphabet = [chr(n) for n in range(97, 123)]
        res = list()
        # 先组织所有字母字符
        for i in alphabet:
            for j in pure_strings:
                if j.lower() == i:
                    res.append(j)
        # 再插入非字母字符
        length = len(strings)
        for k in range(length):
            if not strings[k].isalpha():
                res.insert(k, strings[k])
        print(''.join(res))
    except:
        break