# https://rosettacode.org/wiki/Duffinian_numbers

def sigma_sum(n: int) -> int:
    divisors = [1, n]
    for i in range(2, n // 2 + 2):
        if n % i == 0: divisors.append(i)

    return sum(divisors)

def are_relative_primes(x: int, y: int) -> bool:
    s = min(x, y)
    for i in range(2, s // 2 + 1):
        if x % i == 0 and y % i == 0:
            return False
    return True

def check_composite(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return True
    return False

def check_duffinian(n: int) -> bool:
    return check_composite(n) and are_relative_primes(n, sigma_sum(n))

def check_duffinian_triplet(n: int) -> bool:
    return check_duffinian(n) and check_duffinian(n + 1) and check_duffinian(n + 2)

def get_first_n_duffinian(n: int) -> list[int]:
    items = []
    i = 1
    while len(items) != n:
        if check_duffinian(i): items.append(i)
        i += 1

    return items

def get_first_n_duffinian_triplets(n: int) -> list[tuple[int, int, int]]:
    items = []
    i = 0
    while len(items) != n:
        if check_duffinian_triplet(i): items.append((i, i + 1, i + 2))
        i += 1

    return items

def format_nums(nums: list[int] | list[tuple[int, int, int]], *, rows=5):
    if isinstance(nums[0], int):
        spacing = len(str(nums[-1])) + 1

        for i in range(0, len(nums), rows):
            yield " ".join(f'{j:{spacing}}' for j in nums[i:i+rows])

    elif isinstance(nums[0], tuple):
        spacing = len(str(nums[-1][-1])) + 1

        for tup in nums:
            yield " ".join(f'{i:< {spacing}}' for i in tup)

def main():
    print('First 50 Duffinian numbers:', *format_nums(get_first_n_duffinian(50), rows=10), sep='\n')
    print()
    print('First 15 Duffinian triplets', *format_nums(get_first_n_duffinian_triplets(15)), sep='\n')

if __name__ == '__main__':
    main()
