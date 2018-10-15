def make_bricks(small, big, goal):
  x = goal / 5
  return (big >= x and x * 5 + small >= goal) or (big < x and big * 5 + small >= goal)