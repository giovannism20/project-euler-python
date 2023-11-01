import math

def is_prime(number):
  if number <= 1: return False
  for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0: return False
  return True

def largest_prime_factor(value):
  if value <= 1: return None

  if is_prime(value): return value

  max_prime = 2
  for i in range(2, int(math.sqrt(value)) + 1):
    if value % i == 0:
      factor = value // i
      if is_prime(factor):
        return factor
      elif is_prime(i):
        max_prime = i
  return max_prime

print(largest_prime_factor(600851475143))
