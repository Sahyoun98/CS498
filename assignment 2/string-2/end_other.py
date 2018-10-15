def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  less = len(a)
  if less > len(b):
    less = len(b)
    
  for i in range(-less, 0, 1):
    if a[i] != b[i]:
      return False
  return True