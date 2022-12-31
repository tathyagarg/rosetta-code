# https://rosettacode.org/wiki/Zumkeller_numbers

from itertools import chain, combinations

def can_be_partitioned(nums: list[int]) -> bool:
    xs = list(chain(*[combinations(nums, i) for i in range(1, (len(nums) // 2)+1)]))
    pairs = [(sum(x), sum(set(nums) - set(x))) for x in xs]

    return any(i == j for i, j in pairs)

def get_factors(n: int) -> list:
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return factors

def check_zumkeller(n: int) -> bool:
    return can_be_partitioned(get_factors(n))

def generate_zumkeller(size: int) -> list[int]:
    g = 0
    curr = 0
    while g != size:
        if check_zumkeller(curr):
            g += 1
            yield curr
        curr += 1

    return nums

def main():
    for i, n in enumerate(generate_zumkeller(220), 1):
        print(str(n).ljust(4), end=' ' if i % 10 else '\n')

if __name__ == '__main__':
    main()

