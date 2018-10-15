def close_far(a, b, c):
  y = [a, b, c]
  y.sort()
  is_close = False
  is_far = False
  
  if(y[1] - y[0] < 2):
    is_close = True
  else:
    is_far = True
  
  if(y[2] - y[1] < 2):
    is_close = True
  else:
    is_far = True
    
  return is_far and is_close