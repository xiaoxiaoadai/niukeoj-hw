lists = list(('3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'joker', 'JOKER'))
l = input()
A = l.split('-')[0]
A = A.split(' ')
B = l.split('-')[1]
B = B.split(' ')


# A B 是两个列表
def mysort(A, B):
    if 'joker JOKER'.split(' ') in (A, B):
        if A == ['joker', 'JOKER']:
            return A
        else:
            return B
    if len(A) == len(B):
        if lists.index(A[0]) >= lists.index(B[0]):
            return A
        else:
            return B
    elif len(A) == 4 or len(B) == 4:
        if len(A) == 4:
            return A
        return B
    else:
        return 'ERROR'


result = mysort(A, B)
if result == 'ERROR':
    print('ERROR')
else:
    print(' '.join(result))

