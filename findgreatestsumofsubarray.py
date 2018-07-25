data = input().split()
print(data, type(data))
res = {}


def mysum(l):
    res1 = 0
    for j in l:
        print(j, type(j))
        res1 += int(j)
    return res1


for i in range(len(data)):
    res[i] = mysum(data[:i+1])

for i in res.keys():
    if res[i] == max(res.values()):
        print(res[i])
        print('第%d个' % (i+1))

