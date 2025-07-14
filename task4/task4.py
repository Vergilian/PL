import sys


def read_numbers(filename):
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]


def min_moves_to_equal(nums):
    nums.sort()
    n = len(nums)
    median = nums[n // 2] if n % 2 == 1 else nums[(n // 2) - 1]
    return sum(abs(x - median) for x in nums)


filename = sys.argv[1]
nums = read_numbers(filename)
print(min_moves_to_equal(nums))
