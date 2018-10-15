def array123(nums):
  x = [1 for i in range(len(nums)) if nums[i:i+3] == [1, 2, 3]]
  return len(x) != 0