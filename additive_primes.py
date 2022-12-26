# https://rosettacode.org/wiki/Additive_primes

def check_prime(n: int) -> bool:
    if n == 1: return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def get_digit_sum(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def get_additive_primes(limit: int = 500) -> list[int]:
    return [i for i in range(1, limit + 1) if check_prime(i) and check_prime(get_digit_sum(i))]

def main():
    nums = get_additive_primes()
    print(*nums)

    print(f"There are {len(nums)} Additive Primes under 500")

if __name__ == '__main__':
    main()

