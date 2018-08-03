#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        I = input().split(" ")
        R = input().split(" ")
        R = R[1:]
        R_value = R
        R = list(enumerate(R))
        # TODO: 先把R处理一下：按值从小到大排列，且剔除序号大的重复值
        tmp_i = list()
        tmp_r = list()
        for m in range(len(R)):
            # 去重
            if R[m][1] not in tmp_i:
                tmp_i.append(R[m][1])
                tmp_r.append(R[m])
        R = tmp_r
        tmp = list()
        for m in range(len(R)):
            # 排序
            if R[m][1] not in tmp:
                if len(tmp) == 0:
                    tmp.append(R[m])
                else:
                    for n in range(len(tmp)):
                        if R[m][1] < tmp[n][1]:
                            tmp.insert(n, R[m])
                            break
                        elif n == len(tmp)-1:
                            tmp.append(R[m])
        # TODO: 要不要重新赋值R？tmp已经排好序
        R = tmp
        I = I[1:]
        res = list()
        for i in range(len(R)):
            res_i = list()
            count_i = 0
            for j in range(len(I)):
                if R[i][1] in I[j]:
                    count_i += 1
                    res_i.append(j)
                    res_i.append(I[j])
            if count_i != 0:
                res.append(R[i][1])
                res.append(count_i)
                for p in res_i:
                    res.append(p)
        print(str(len(res))+" "+" ".join(res))
    except:
        break