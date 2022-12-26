proc check_prime(n: int): bool =
  if n == 1: return false

  for i in 2..n div 2:
    if n mod i == 0: return false
  return true

proc digit_sum(n: int): int =
  var
    total = 0
    v = n
  while v > 0:
    total += v mod 10
    v = v div 10
  return total

proc additive_primes(limit: int = 500): seq[int] =
  var items: seq[int] = @[]
  for i in 1..(limit + 1):
    if check_prime(i) and check_prime(digit_sum(i)):
      items.add(i)
  return items

proc main() =
  var nums = additive_primes()
  for i in nums:
    stdout.write i, " "
  echo ""
  echo "Found ", nums.len, " additive primes under 500"

main()

