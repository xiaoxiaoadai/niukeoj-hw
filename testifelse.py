#!/usr/bin/env python3

a = 'abcdefghijklmn'

if a[-1] == 'n':
    print('yes')
else:
    print('no')

b = True if a[-1] == 'x' else False

print(b)