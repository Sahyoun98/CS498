def string_splosion(str):
  x = [str[j] for i in range(len(str)) for j in range(i + 1)]
  x = "".join(x)
  return x