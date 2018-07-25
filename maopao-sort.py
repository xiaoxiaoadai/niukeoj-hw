import random
list_data = []
for i in range(10):
    list_data.append(random.randint(0, 20))

list_len = len(list_data) - 1
# 原始列表
print(list_data)

for i in range(10):
    for j in range(list_len - i):
        if list_data[j] > list_data[j + 1]:
            tmp = list_data[j]
            list_data[j] = list_data[j + 1]
            list_data[j + 1] = tmp
print(list_data)