def array_front9(nums):
  length = len(nums)
  if length > 4:
    length = 4
  x = [1 for i in range(length) if nums[i] == 9]
  return len(x) != 0
