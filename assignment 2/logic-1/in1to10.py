def in1to10(n, outside_mode):
  tmp = n > 0 and n < 11
  if outside_mode and (n != 1 and n != 10):
    tmp = not tmp
  return tmp