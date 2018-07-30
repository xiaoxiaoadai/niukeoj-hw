#!/usr/bin/env python3
# -*- coding:utf-8 -*-

A, B, C, D, E, F, G = 0, 0, 0, 0, 0, 0, 0
"""
F:IP或掩码错误
G:私有IP
"""
res = list()
while True:
    try:
        inputs = input()
        if inputs is '':
            # print('{A} {B} {C} {D} {E} {F}'.format(**locals()))
            break
        [IP, MASK] = inputs.split('~')
        res.append([IP, MASK])
    except:
        break

for [ip, mask] in res:
    ip = ip.split('.')
    mask = mask.split('.')
    # IP错误
    if '' in ip:
        F += 1
        continue
    else:
        a = int(ip[0])
        b = int(ip[1])
        c = int(ip[2])
        d = int(ip[3])
        if not (0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255):
            F += 1
            continue
        elif (a, b, c, d) == (0, 0, 0, 0) or (a, b, c, d) == (255, 255, 255, 255):
            F += 1
            continue
        elif a == 0:
            continue
        else:
            # 掩码错误
            if '' in mask or mask == ['255', '255', '255', '255']:
                F += 1
                continue
            else:
                # 需要满足“子网掩码为前面是连续的1，然后全是0”
                # FIXME: lstrip在这里竟然把我的'0b0' strip成了''
                # FIXME: '00000001'会被输出为'1'，避免11111111 00000001 00000000 00000000这种不合格掩码
                # mask = [bin(int(i)).lstrip('0b') or '0' for i in mask]
                tmp = list()
                for i in mask:
                    i = bin(int(i)).lstrip('0b') or '0'
                    if len(i) != 8:
                        i = '0'*(8 - len(i)) + i
                    tmp.append(i)
                # mask = tmp
                if '01' in ''.join(tmp):
                    F += 1
                    continue
            # IP合法的前提下计数
            if 1 <= a <= 126:
                A += 1
                if a == 10:
                    G += 1
            elif 128 <= a <= 191:
                B += 1
                if a == 172 and 16 <= b <= 31:
                    G += 1
            elif a <= 223:
                C += 1
                if a == 192 and b == 168:
                    G += 1
            elif a <= 239:
                D += 1
            else:
                E += 1


print('{A} {B} {C} {D} {E} {F} {G}'.format(**locals()))
