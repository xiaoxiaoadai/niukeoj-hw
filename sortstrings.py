#!/usr/bin/env python3

lists = []
l = input()
#print(l)
for i in l:
    if i in lists:
        continue
    lists.append(i)

print(''.join(lists))
# SoriEYVzZDtnWCFAKUONgPaplIybQHmdddddM