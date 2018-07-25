# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        print('numbers:', numbers, type(numbers))
        print(len(numbers))
        if len(numbers) == 1:
            print('xxxxxx')
            return int(numbers)
        res = {}
        a = len(numbers) / 2
        for i in numbers:
            if i in res.keys():
                res[i] += 1
                if int(res[i]) > a:
                    return i
            else:
                res[i] = 1
        return 0


a = Solution()
data = input()
print(a.MoreThanHalfNum_Solution(data))