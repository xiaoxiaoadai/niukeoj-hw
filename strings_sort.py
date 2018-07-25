#!/usr/bin/env python3

n = 2
arr = ['12 ', '123']
#print(''.join(sorted(arr, lambda x, y : -cmp(x+y, y+x))))
def mysort(a, b):
    if int(str(a)+str(b)) >= int(str(b)+str(a)):
        return a
    return b

lists = []
for j in range(0, int(n)):
        for i in range(0, int(n)):
            if i == j:
                continue
            maxi = mysort(arr[i], arr[j])
        lists.append(str(maxi))
print(''.join(lists))