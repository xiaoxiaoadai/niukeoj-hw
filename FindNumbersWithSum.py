# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        a = [x for x in array]
        b = [tsum-x for x in array]
        res = []
        for i in b:
            if i in a:
                if i > tsum - i:
                    res.append([tsum-i, i])
                else:
                    res.append([i, tsum-i])
        def mysort(l):
            #temp = l[0]
            for i in range(len(l)):
                for j in range(i+1,len(l)):
                    if l[i][0]*l[i][1] > l[j][0]* l[j][1]:
                        temp = l[i]
                        l[i] = l[j]
                        l[j] = temp
            return l[0]

        if len(res) > 1:
            res2 = mysort(res)
            return res2
        return res

array = [1,2,3,4,5,6,7,8,9,10]
tsum = 11
print(Solution().FindNumbersWithSum(array=array, tsum=15))