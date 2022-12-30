# https://rosettacode.org/wiki/Extra_primes

def check_prime(n: int) -> bool:
    if n <= 1: return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_extra_prime(n: int) -> bool:
    return (
        check_prime(n) and
        all(check_prime(int(i)) for i in str(n)) and
        check_prime(sum(map(int, str(n))))
    )

def generate_extra_primes(max_num: int) -> list[int]:
    return [i for i in range(1, max_num) if check_extra_prime(i)]

def main():
    print(*generate_extra_primes(10_000))

if __name__ == '__main__':
    main()
