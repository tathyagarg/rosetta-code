def get_factors(n: int) -> list[int]:
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def get_tracks(limit: int):
    d, p, a = 0, 0, 0

    for i in range(1, limit + 1):
        factors = get_factors(i)
        factor_sum = sum(factors)

        if factor_sum < i: d += 1
        elif factor_sum == i: p += 1
        elif factor_sum > i: a += 1

    return d, p, a

def main():
    limit = 20_000
    tracks = get_tracks(limit)
    for num_type, count in zip(['deficient', 'perfect', 'abundant'], tracks):
        print(f'Number of {num_type} numbers under {limit}: {count}')

if __name__ == '__main__':
    main()
