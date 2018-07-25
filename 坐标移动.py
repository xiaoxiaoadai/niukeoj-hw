#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def check(string):
    if string == '':
        return False
    t = list(string)
    start = t.pop(0)
    if start in ['A', 'W', 'D', 'S'] and ''.join(t).isdigit():
            return True
    return False

def doA(a, init=[0, 0]):
    init[0] -= a

def doD(d, init=[0, 0]):
    init[0] += d

def doW(w, init=[0, 0]):
    init[1] += w

def doS(s, init=[0, 0]):
    init[1] -= s


while True:
    try:
        init = [0, 0]
        res = list()
        strings = input().strip(';').split(';')
        for i in strings:
            if check(i):
                res.append(i)
        for i in res:
            i = list(i)
            x = i.pop(0)
            i = int(''.join(i))
            if x == 'A':
                doA(i, init)
            elif x == 'D':
                doD(i, init)
            elif x == 'W':
                doW(i, init)
            elif x == 'S':
                doS(i, init)

        print('{0},{1}'.format(init[0], init[1]))
    except:
        break