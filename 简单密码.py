#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        string = input()
        res = list()
        for i in string:
            if i.isdigit():
                res.append(i)
            elif i.isupper():
                if i == 'Z':
                    res.append('a')
                else:
                    res.append(chr(ord(i.lower())+ 1))
            elif i.islower():
                if i in 'abc':
                    res.append('2')
                elif i in 'def':
                    res.append('3')
                elif i in 'ghi':
                    res.append('4')
                elif i in 'jkl':
                    res.append('5')
                elif i in 'mno':
                    res.append('6')
                elif i in 'pqrs':
                    res.append('7')
                elif i in 'tuv':
                    res.append('8')
                elif i in 'wxyz':
                    res.append('9')
        print("".join(res))
    except:
        break