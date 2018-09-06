#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def check_ip(ip):
    """
    check ip
    :param ip:str: 'A.B.C.D'
    :return:boolean: true or false
    """
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return False

    ip_list = [int(i) for i in ip_list]
    a, b, c, d = ip_list
    # print(a, b, c, d)
    if a==b==c==d==0 or a==b==c==d==255:
        return False
    if a not in range(0,256) or b not in range(0,256) or c not in range(0,256) or d not in range(0,256):
        return False

    return True

def check_mask(mask):
    """
    check mask
    :param mask:str: 'A.B.C.D'
    :return:boolean: true or false
    """
    mask_list = mask.split('.')
    if len(mask_list) != 4:
        return False
    mask_list = [int(j) for j in mask_list]
    a, b, c, d = mask_list
    # print(a,b,c,d)
    if a==b==c==d==0 or a==b==c==d==255:
        return False
    if a not in range(0,256) or b not in range(0,256) or c not in range(0,256) or d not in range(0,256):
        return False
    a = str(bin(a)).lstrip('0b').rjust(8, '0')
    b = str(bin(b)).lstrip('0b').rjust(8, '0')
    c = str(bin(c)).lstrip('0b').rjust(8, '0')
    d = str(bin(d)).lstrip('0b').rjust(8, '0')
    # print(a, b, c, d)
    temp = str(a)+str(b)+str(c)+str(d)
    if '01' in temp:
        return False
    return True


while True:
    try:
        strings = input().split()
        mask = strings[0]
        ip_a = strings[1]
        ip_b = strings[2]
        if check_mask(mask) and check_ip(ip_a) and check_mask(ip_b):
            mask = [i.split('.') for i in mask]
            ip_a = [j.split('.') for j in ip_a]
            ip_b = [k.split('.') for k in ip_b]

            res_a = ''
            res_b = ''

            for m in range(4):
                res_a += str((int(mask[m])) & int(ip_a[m]))
                res_b += str((int(mask[m])) & int(ip_b[m]))
            if res_a == res_b:
                print(0)
            else:
                print(2)
        else:
            print(1)
    except:
        break

