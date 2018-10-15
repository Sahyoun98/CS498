def pos_neg(a, b, negative):
  if negative == True:
    return a < 0 and b < 0
  return a * b < 0