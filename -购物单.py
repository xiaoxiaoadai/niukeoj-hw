#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import copy


while True:
    try:
        # [总预算N, 总件数m]
        [N, m] = input().split()
        N = int(N)
        m = int(m)
        res = list()
        for i in range(1, m+1):
            res_list = input().split()
            res_list = [int(j) for j in res_list]
            res.append(res_list)
        # 需要用深拷贝，否则tmp会影响res
        # 深拷贝：申请额外的内存空间来存储一份拷贝
        tmp = copy.deepcopy(res)
        for item in res:
            # 价格v
            v = item[0]
            p = item[1]
            q = item[2]
            if v > N:
                # 剔除太贵的主件以及附件
                tmp.remove(item)
                continue
            # print(res[q-1][2])
            # print(res[q-1][0])
            if q != 0 and res[q-1][0] + v > N:
                # 剔除主附件总价太贵的附件
                tmp.remove(item)
        final_res = tmp[0][0]
        for i in range(len(tmp)):
            tmp[i][0] > final_res
            final_res = tmp[i][0]
            for j in range(i+1, len(tmp)):
                #TODO: 从tmp中计算在满足总预算前提下的最大的v*p和
        print("res: {0}; tmp:{1}".format(res, tmp))

    except:
        break