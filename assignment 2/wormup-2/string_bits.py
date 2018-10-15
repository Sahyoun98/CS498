def string_bits(str):
  x = [str[i] for i in range(len(str)) if i % 2 == 0]
  x = "".join(x)
  return x