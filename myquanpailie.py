# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
    def Permutation(self, ss):
        # write code here
        ss = ss.split()
        if len(ss) <= 1:
            return list(ss)
        self.res = []
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                self.res.append(ss[i] + j)
            #count += 1
        return self.res


a = Solution()
data = input().strip()
#print(data)
print(a.Permutation(data))