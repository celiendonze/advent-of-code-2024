from pathlib import Path

import numpy as np

input_path = Path(__file__).parent.parent / "data/inputs/day_2/input.txt"

lines = input_path.read_text().split("\n")


def is_problem_safe(numbers: np.ndarray) -> bool:
    diff = np.diff(numbers)
    return all(diff > 0) and all(diff <= 3) or all(diff < 0) and all(diff >= -3)


number_safe = 0
for line in lines:
    if not line:
        continue
    numbers = np.array([int(x) for x in line.split(" ")])
    if is_problem_safe(numbers):
        number_safe += 1

print("number of safe lines:")
print(number_safe)

number_safe = 0
for line in lines:
    if not line:
        continue
    numbers = np.array([int(x) for x in line.split(" ")])
    if is_problem_safe(numbers):
        number_safe += 1
        continue
    inner_number_not_safe = 0
    for i in range(len(numbers)):
        smaller_numbers = np.delete(numbers, i)
        if is_problem_safe(smaller_numbers):
            number_safe += 1
            break

print("number of safe lines (part 2):")
print(number_safe)
