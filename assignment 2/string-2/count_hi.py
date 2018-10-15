def count_hi(str):
  x = list([1 for i in range(len(str) - 1) if str[i] == "h" and str[i + 1] == "i"])
  return len(x)