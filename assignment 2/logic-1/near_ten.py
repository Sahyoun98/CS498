def near_ten(num):
  x = num / 10 * 10
  y = (num / 10 + 1) * 10
  return y - num < 3 or num - x < 3