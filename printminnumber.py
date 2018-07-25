# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, data):
        # write code here
        numbers = []
        for i in data:
            if type(i) == 'int':
                numbers.append(str(i))
            else:
                numbers.append(i)
        print('numbers:',numbers)
        temp = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if int(str(numbers[i]) + str(numbers[j])) > int(str(numbers[j]) + str(numbers[i])):
                    print('xxxxxxxx')
                    temp = numbers[i]
                    numbers[i] = str(numbers[j])
                    numbers[j] = str(temp)
        for i in range(len(numbers)):
            numbers[i] = str(numbers[i])
        return ''.join(numbers)


a = Solution()
# data = raw_input().strip('[').strip(']').split(',')
data = input().strip('[').strip(']').split(',')
print('"' + a.PrintMinNumber(data) + '"')