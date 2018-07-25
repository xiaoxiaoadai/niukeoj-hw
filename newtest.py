# -*- coding:utf-8 -*-
line = input().split('、')
c = line[0]
c = int(c)
b = line[1]
b = int(b)

lists = line[2:]

res = {}
x = 0

for i in lists:
    i = int(i)
    x = i % b
    if x < c:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
print(max(res.values()))