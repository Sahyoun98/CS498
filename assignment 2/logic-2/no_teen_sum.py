def no_teen_sum(a, b, c):
  x = [a, b, c]
  tmp = [15, 16]
  sol = list([i for i in x if (i < 13 or i > 19) or i in tmp])
  sol.append(0)
  return reduce(lambda x, y: x + y, sol)