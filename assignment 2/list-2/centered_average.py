def centered_average(nums):
  nums.sort()
  sum = reduce(lambda x, y: x + y, nums[1:-1])
  return sum / (len(nums) - 2)
