from pathlib import Path

import numpy as np

input_path = Path(__file__).parent.parent / "data/inputs/day_2/input.txt"

lines = input_path.read_text().split("\n")

number_safe = 0
for line in lines:
    if not line:
        continue
    numbers = np.array([int(x) for x in line.split(" ")])
    diff = np.diff(numbers)
    if all(diff > 0) and all(diff <= 3) or all(diff < 0) and all(diff >= -3):
        number_safe += 1

print("number of safe lines:")
print(number_safe)
