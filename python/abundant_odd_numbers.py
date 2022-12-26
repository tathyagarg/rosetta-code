def get_factors(n: int) -> list[int]:
    factors = []
    for num in range(1, int(n // 2) + 2):
        if n % num == 0:
            factors.append(num)
    return factors

def main(nums: int = 25):
    i = 0
    v = 1
    while i < nums:
        q = get_factors(v)
        if sum(q) > v:
            print(f'Abundant odd number {i+ 1}: {v} proper divisor sum = {sum(q)}')
            i += 1
        v += 2

if __name__ == '__main__':
    main()
