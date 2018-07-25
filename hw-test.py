# -*- encoding:utf-8 -*-
line = input().split('、')
#input: 5、2、1、2、3、4、6、7、8、9、10
c = line[0]
c = int(c)
b = line[1]
b = int(b)
lists = line[2:]
print(lists)
count = 0
# 把lists列表内容转四字节的列表，并将这四个字节组成列表；每个数据变成了长为4 的列表
for i in lists:
    lists[count] = list(int(i).to_bytes(length=4,byteorder='big'))
    count += 1

print(lists)

res = {}
x = 0
for i in lists:
    #i = int(i)
    x = sum(i)% b
    if x < c:
        if x in res.keys():
            res[x] += 1
        else:
            res[x] = 1

print(res)
print(max(res.values()))