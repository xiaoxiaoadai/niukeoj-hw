def josephus(n):
  m = 3
  if type(n) != type(1) or n <= 0:
    raise Exception('n must be an integer(n > 0)')
  if n == 1:
    return 0
  else:
    print('===', n)
    return (josephus(n - 1) + m) % n
if __name__ == '__main__':
  print(josephus(8))
  #print(josephus(1, 2))
  #print(josephus(0, 2))
