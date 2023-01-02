import std/math
import std/strformat

proc check_condition(n: int): bool =
    return n^2 - (n - 1) ^ 2 > 1000

proc get_lowest(): int =
    var curr: int = 0
    while true:
        if check_condition(curr): return curr
        inc curr

proc main() =
    echo fmt"The smallest number that satisfies the condition is: {get_lowest()}"

main()
