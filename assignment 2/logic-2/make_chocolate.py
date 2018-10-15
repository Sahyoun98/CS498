def make_chocolate(small, big, goal):
  if big * 5 + small < goal:
    return -1
  
  x = goal / 5
  if big < x:
    x = big
    
  if small >= goal - x * 5:
    return goal - x * 5
    
  return -1