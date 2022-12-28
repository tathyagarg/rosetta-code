import std/math

proc check_narc(n: int): bool =
  var
    num_size: int = 0
    total: int = 0
    d = n
    v = d

  while v > 0:
    v = v div 10
    inc num_size

  while d > 0:
    total += (d mod 10) ^ num_size
    d = d div 10

  return total == n

proc generate_narcs(size: int): seq[int] =
  var
    items: seq[int]
    curr: int = 0

  while items.len != size:
    if check_narc(curr): items.add(curr)
    inc curr

  return items

proc main() = echo generate_narcs(15)

main()
