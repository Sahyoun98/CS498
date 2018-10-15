def caught_speeding(speed, is_birthday):
  x = 0
  if is_birthday:
    x = 5
  
  if speed > 80 + x:
    return 2
  if speed > 60 + x:
    return 1
  return 0