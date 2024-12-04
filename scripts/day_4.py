import re
from pathlib import Path

import numpy as np

input_path = Path(__file__).parent.parent / "data/inputs/day_4/input.txt"

text = input_path.read_text()
# text = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """.strip()
lines = text.split("\n")
array = np.array([list(line) for line in lines if line])

# pad array with empty strings
array = np.pad(array, 3, constant_values="")

w = array.shape[1]
h = array.shape[0]

count = 0
for i in range(h):
    for j in range(w):
        if array[i, j] == "X":
            words_4_letters = [
                array[i, j] + array[i, j + 1] + array[i, j + 2] + array[i, j + 3],
                array[i, j] + array[i, j - 1] + array[i, j - 2] + array[i, j - 3],
                array[i, j] + array[i + 1, j] + array[i + 2, j] + array[i + 3, j],
                array[i, j] + array[i - 1, j] + array[i - 2, j] + array[i - 3, j],
                array[i, j]
                + array[i + 1, j + 1]
                + array[i + 2, j + 2]
                + array[i + 3, j + 3],
                array[i, j]
                + array[i - 1, j - 1]
                + array[i - 2, j - 2]
                + array[i - 3, j - 3],
                array[i, j]
                + array[i + 1, j - 1]
                + array[i + 2, j - 2]
                + array[i + 3, j - 3],
                array[i, j]
                + array[i - 1, j + 1]
                + array[i - 2, j + 2]
                + array[i - 3, j + 3],
            ]
            for word in words_4_letters:
                if "XMAS" in word:
                    count += 1
                if "SAMX" in word:
                    count += 1

print("Number of XMAS:", count)

count = 0
for i in range(h):
    for j in range(w):
        # print(f"({i},{j})", end=" ")
        if array[i, j] == "A":
            word = (
                array[i - 1, j - 1]
                + array[i - 1, j + 1]
                + array[i, j]
                + array[i + 1, j - 1]
                + array[i + 1, j + 1]
            )
            if word in ["MMASS", "MSAMS", "SSAMM", "SMASM"]:
                count += 1
    # print()

print("Number of SAM:", count)
