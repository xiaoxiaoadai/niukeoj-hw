#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        R = input().split(" ")
        I = input().split(" ")
        R = R[1:]
        I = I[1:]
        res = dict()
        for i in range(len(R)):
            count = 0
            for j in range(len(I)):
                if R[i] in I[j]:
                    print(R[i])
                    count += 1
                    res[I[j]] = j

            print(count)
            print(res[i])
            print(I[res[i]])

    except:
        break