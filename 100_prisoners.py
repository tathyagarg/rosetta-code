# https://rosettacode.org/wiki/100_prisoners
import random
from typing import Callable

def run_checks(f):
    return f.__code__.co_argcount == 2


def create_prisoners():
    prisoners = list(range(1, 101))
    boxes = dict(zip(random.sample(range(1, 101), 100), range(1, 101)))
    return prisoners, boxes

def naive_strategy(prisoners: list[int], boxes: dict[int, int]):
    for prisoner in prisoners:
        for i in range(50):
            box_opened = random.randint(1, 100)
            if boxes[box_opened] == prisoner:
                break
        else:
            return False
    return True

def smart_strategy(prisoners: list[int], boxes: dict[int, int]):
    for prisoner in prisoners:
        box_opened = prisoner
        for i in range(50):
            if (b := boxes[box_opened]) == prisoner:
                break
            box_opened = b
        else:
            return False
    return True

def run_strategy(strategy: Callable, iterations: int = 10_000):
    if not run_checks(strategy):
        return ValueError('Invalid function')

    success = 0
    for i in range(iterations):
        success += int(strategy(*create_prisoners()))
    return (success / iterations) * 100

def main(_round=2):
    print(f"Naive strategy success rate: {run_strategy(naive_strategy):.{_round}f}%")
    print(f"Smart strategy success rate: {run_strategy(smart_strategy):.{_round}f}%")

if __name__ == '__main__':
    main()


