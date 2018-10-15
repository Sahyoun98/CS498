def round_sum(a, b, c):
  helper = lambda x: (x + 5) / 10 * 10
  return helper(a) + helper(b) + helper(c)