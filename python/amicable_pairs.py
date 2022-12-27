# https://rosettacode.org/wiki/Amicable_pairs

MAX_NUM = 20_000

def proper_divisors(n: int) -> list[int]:
    nums = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            nums.append(i)

    return nums

def amicable_pairs(i: int):
    yielded = []
    for n in range(i):
        m = sum(proper_divisors(n))
        if n != m and sum(proper_divisors(m)) == n and (m, n) not in yielded:
            yield n, m
            yielded.append((n, m))

def display(nums):
    spacing = len(str(MAX_NUM)) + 1
    for i, j in nums:
        print(f'{i:{spacing}} {j:{spacing}}')

def main():
    display(amicable_pairs(MAX_NUM))

if __name__ == '__main__':
    main()
