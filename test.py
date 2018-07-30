#!/usr/bin/python3
import sys
# 记录所有Log,若超过8行输出时只取最新的8条！
log_dict = {}
idx_list = []
while True:
    try:
        line = sys.stdin.readline()
        if len(line) == 8 or line == '' or line == '\n':
            break
        path, num = line.split()
        file_name = path.split('\\')[-1]
        if len(file_name) > 16:
            file_name = file_name[-16:]
        idx = file_name + " " + num
        if idx in log_dict.keys():
            log_dict[idx] += 1
        else:
            log_dict[idx] = 1
            idx_list.append(idx)
    except:
        break
out_list = idx_list[-8:]
for idx in out_list:
    print(idx + " " + str(log_dict[idx]))