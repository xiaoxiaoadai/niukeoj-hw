# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = data.count(k)
        return count


a = Solution()
inputs = input().split(',')
data = inputs[:-2]
print('data',data)
k = inputs[-1]
print('k',k)
print(a.GetNumberOfK(data, k))