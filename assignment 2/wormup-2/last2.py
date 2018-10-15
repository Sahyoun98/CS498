def last2(str):
  x = [1 for i in range(len(str) - 2) if str[i:i+2] == str[-2:]]
  return len(x)