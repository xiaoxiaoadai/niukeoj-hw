def fun1(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in fun1(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl


def main():
    ss = input()
    a = fun1(ss)
    #print(len(a), a)
    print(a)
    pass


if __name__ == '__main__':
    main()