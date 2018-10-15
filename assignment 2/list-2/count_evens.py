def count_evens(nums):
  nums = list(filter(lambda x: x % 2 == 0, nums))
  
  return len(nums)