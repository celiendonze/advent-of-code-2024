from pathlib import Path

from tqdm import tqdm

day_7_input = Path("data/inputs/day_7/input.txt").read_text().strip().split("\n")

lines = []
for line in day_7_input:
    result, numbers = line.split(":")
    numbers = numbers.strip().split(" ")
    numbers = [int(x) for x in numbers]
    lines.append((int(result), numbers))


def is_possible(numbers: list[int], target: int, use_concat: bool = False) -> bool:
    def backtrack(index, current_value):
        if index == len(numbers):
            return current_value == target
        # Try adding the next number
        if backtrack(index + 1, current_value + numbers[index]):
            return True
        # Try multiplying the next number
        if backtrack(index + 1, current_value * numbers[index]):
            return True
        if use_concat:
            # Try concatenating the next number
            if backtrack(index + 1, int(str(current_value) + str(numbers[index]))):
                return True
        return False

    # Start the recursion from the first number
    return backtrack(1, numbers[0])


if __name__ == "__main__":
    result_sum = 0
    for line in tqdm(lines):
        result, numbers = line
        if is_possible(numbers, result):
            result_sum += result

    print("Part 1:")
    print(result_sum)

    result_sum = 0
    for line in tqdm(lines):
        result, numbers = line
        if is_possible(numbers, result, use_concat=True):
            result_sum += result

    print("Part 2:")
    print(result_sum)
