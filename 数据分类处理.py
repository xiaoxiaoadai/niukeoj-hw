#!/usr/bin/env python3
# -*- coding:utf-8 -*-

while True:
    try:
        I = input().split(" ")
        R = input().split(" ")
        R = R[1:]
        R_value = R
        R = list(enumerate(R))
        # tmp_i 原序列中的值，用来做成员运算
        tmp_i = list()
        # tmp_r 用来保存去重后的R
        tmp_r = list()
        for m in range(len(R)):
            # 去重
            if R[m][1] not in tmp_i:
                tmp_i.append(R[m][1])
                tmp_r.append(R[m])
        R = tmp_r
        # tmp = list()
        '''for m in range(len(R)):
            # 排序
            if R[m][1] not in tmp:
                if len(tmp) == 0:
                    tmp.append(R[m])
                else:
                    for n in range(len(tmp)):
                        if int(R[m][1]) < int(tmp[n][1]):
                            tmp.insert(n, R[m])
                            break
                        else:
                            tmp.append(R[m])
        '''
        # 对R进行冒泡排序
        for x in range(len(R)):
            for y in range(x+1, len(R)):
                if int(R[x][1]) > int(R[y][1]):
                    R[x], R[y] = R[y], R[x]
        # R 排好序
        # R = tmp
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
        res = [str(x) for x in res]
        print(str(len(res))+" "+" ".join(res))
    except:
        break