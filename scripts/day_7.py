from itertools import combinations_with_replacement, permutations
from pathlib import Path

import numpy as np
from tqdm import tqdm

day_7_input = Path("data/inputs/day_7/input.txt").read_text().strip().split("\n")
print(len(day_7_input))
day_7_input = day_7_input[:20]


lines = []
for line in day_7_input:
    result, numbers = line.split(":")
    numbers = numbers.strip().split(" ")
    numbers = [int(x) for x in numbers]
    lines.append((int(result), numbers))


def is_possible(numbers: list[int], target: int) -> bool:
    if eval("+".join([str(x) for x in numbers if x > 1])) > target:
        return False
    if eval("*".join([str(x) for x in numbers])) < target:
        return False

    all_operations = set()
    all_combinations = list(combinations_with_replacement("+*", len(numbers) - 1))
    for c in all_combinations:
        all_operations.update(set(permutations(c)))
    # print(len(all_operations))
    for ops in all_operations:
        expression = str(numbers[0])
        for i, op in enumerate(ops):
            expression += f" {op} {numbers[i + 1]}"
        if eval(expression) == target:
            return True
    return False


if __name__ == "__main__":
    result_sum = 0
    for line in tqdm(lines):
        result, numbers = line
        if is_possible(numbers, result):
            result_sum += result

    print("Part 1:")
    print(result_sum)
