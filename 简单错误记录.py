#!/usr/bin/env python3
# -*- coding:utf-8 -*-

res = dict()
f_res = list()
while True:
    try:
        strings = input()
        if strings == '' or strings == '\n':
            break
        [fpath, line] = strings.split(' ')
        fname = fpath.split('\\')[-1]
        if len(fname) > 16:
            fname = fname[-16:]
        fnames = fname + ' ' + line
        if fnames in res:
            res[fnames] += 1
        else:
            res[fnames] = 1
            f_res.append(fnames)

    except:
        break

for i in f_res[-8:]:
    print('{0} {1}'.format(i, res[i]))
