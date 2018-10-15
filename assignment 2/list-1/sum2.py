def sum2(nums):
  nums.append(0)
  nums.append(0)
  return reduce(lambda i, j: i + j, nums[:2])