def sum67(nums):
  stop = False
  
  sum = 0
  for i in nums:
    if stop:
      if i == 7:
        stop = False
      continue
    if i == 6:
      stop = True
      continue
    sum = sum + i
    
  return sum