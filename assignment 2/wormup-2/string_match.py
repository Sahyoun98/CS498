def string_match(a, b):
  length = len(a)
  if length > len(b):
    length = len(b)
  x = [1 for i in range(length - 1) if a[i:i+2] == b[i:i+2]]
  return len(x)