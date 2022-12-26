import std/random
import std/sequtils
import std/strformat
import tables

proc make_boxes(): Table[int, int] =
  var
    boxes = initTable[int, int]()
    keys = toSeq(0..99)

  shuffle(keys)
  for i in 0..99:
    boxes[i] = keys[i]

  return boxes

proc make_prionsers(): seq[int] =
  var
    prionsers = toSeq(0..99)
  shuffle(prionsers)
  return prionsers

proc naive_strategy(prisoners: seq[int], boxes: Table[int, int]): bool =
  var
    box_opened = 0
    prev = newSeq[int]()
    found: bool = false
  for prisoner in prisoners:
    prev = newSeq[int]()
    for i in 1..50:
      box_opened = rand(0..99)
      while box_opened in prev:
        box_opened = rand(0..99)
      prev.add(box_opened)

      if boxes[box_opened] == prisoner:
        break
    if boxes[box_opened] != prisoner:
      return false
  return true

proc smart_strategy(prisoners: seq[int], boxes: Table[int, int]): bool =
  var
    box_opened: int = 0
    b: int = 0
  for prisoner in prisoners:
    box_opened = prisoner
    for i in 1..50:
      b = boxes[box_opened]
      if b == prisoner:
        break
      box_opened = b
    if b != prisoner:
      return false
  return true

proc run_strategy(strategy: proc, iterations: int = 10_000): float =
  var
    success = 0
    c = false
  for i in 0..iterations:
    var
      prisoners = make_prionsers()
      boxes = make_boxes()

    c = strategy(prisoners, boxes)
    success += (int) c

  return (success / iterations) * 100

proc main() =
  randomize()
  echo fmt"Naive strategy success rate: {run_strategy(naive_strategy)}%"
  echo fmt"Smart strategy success rate: {run_strategy(smart_strategy)}%"

main()

