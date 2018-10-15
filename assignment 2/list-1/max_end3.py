def max_end3(nums):
  x = nums[0]
  if x < nums[-1]:
    x = nums[-1]
  x = list(map(lambda i: x, nums))
  return x