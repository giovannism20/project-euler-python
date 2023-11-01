def fibonacci(value):
  a, b = 1,1
  sum = 0
  while b <= value:
    if b % 2 == 0:
      sum += b
    a, b = b, a + b
  return sum

print(fibonacci(4000000))
