# https://rosettacode.org/wiki/Birthday_problem

import random

def calculate_overlap_chances(n: int, iterations: int = 10_000) -> float:
    success = 0

    for i in range(iterations):
        birthdays = set()
        for j in range(n):
            birthdays.add(random.randint(1, 365))
        if len(birthdays) != n: success += 1

    return (success / iterations) * 100


def main():
    print(f'{calculate_overlap_chances(57, 10_000):.4f}%')

if __name__ == '__main__':
    main()
