import std/[strformat, math, random, sets]

proc calc_overlap_chance(n: int, iterations: int = 10_000): float =
    var
      success: int = 0
      birthdays = initHashSet[int]()

    for i in 1..iterations:
        birthdays = initHashSet[int]()
        for j in 1..n:
            randomize()
            birthdays.incl(rand(1..365))
        if birthdays.len != n: success += 1

    return (success / iterations) * 100

proc main() =
    randomize()
    var
      overlap_chance: float = calc_overlap_chance(57, 10_000)
    echo &"Overlap chance: {overlap_chance:.4f}%"

main()
