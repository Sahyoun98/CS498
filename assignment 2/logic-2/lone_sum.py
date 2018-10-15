def lone_sum(a, b, c):
  tmp = [a, b, c]
  tmp.sort()
  tmp.append(tmp[0])
  x = list([tmp[i] for i in range(1, 3) if tmp[i] != tmp[i - 1] and tmp[i] != tmp[i + 1]])
  
  if tmp[0] != tmp[1]:
    x.append(tmp[0])
  else:
    x.append(0)
 
  return reduce(lambda i, j: i + j, x)