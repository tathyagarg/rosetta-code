import std/enumerate

proc get_doors(): array[100, bool] =
  var doors: array[100, bool]

  for n in 1..100:
    for i, door in enumerate(doors):
      if i mod n == 0:
        doors[i] = not doors[i]
  return doors

proc display(items: array[100, bool]) =
  for i, item in enumerate(items):
    if item: stdout.write i, " "

proc main() =
  var nums = get_doors()
  display(nums)

main()
