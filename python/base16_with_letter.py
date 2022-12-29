# https://rosettacode.org/wiki/Base_16_numbers_needing_a_to_f

def generate_nums() -> list[int]:
    items = [i for i in range(1, 501) if any(j in hex(i)[2:] for j in 'abcdef')]
    return items

def format_nums(nums: list[int], rows: int = 10):
    biggest = len(str(max(nums)))

    for i in range(0, len(nums), rows):
        print(' '.join(str(j).ljust(biggest) for j in nums[i:i+rows]))

def main():
    nums = generate_nums()
    format_nums(nums, len(nums)//7)  # 7 columns

if __name__ == '__main__':
    main()
