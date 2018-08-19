#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 加密
def Encrypt(aucString):
    if aucString == '':
        return ''
    res = list()
    for i in aucString:
        if i.isalpha():
            if i.islower():
                if i == 'z':
                    res.append('A')
                    continue
                res.append(chr(ord(i)+1).upper())
            else:
                if i == 'Z':
                    res.append('a')
                    continue
                res.append(chr(ord(i)+1).lower())
        else:
            if i == '9':
                res.append('0')
                continue
            res.append(str(int(i)+1))
    return ''.join(res)

# 解密
def unEncrypt(result):
    if result == '':
        return ''
    res = list()
    for j in result:
        if j.isalpha():
            if j.islower():
                if j == 'a':
                    res.append('Z')
                    continue
                res.append(chr(ord(j)-1).upper())
            else:
                if j == 'A':
                    res.append('z')
                    continue
                res.append(chr(ord(j)-1).lower())
        else:
            if j == '0':
                res.append('9')
                continue
            res.append(str(int(j)-1))
    return ''.join(res)

while True:
    try:
        clear_string = input()
        encrypt_string = input()
        print(Encrypt(clear_string))
        print(unEncrypt(encrypt_string))
    except:
        break