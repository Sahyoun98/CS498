def has23(nums):
  x = [1 for i in nums if i == 2 or i == 3]
  return len(x) != 0