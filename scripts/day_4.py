from pathlib import Path

import numpy as np

input_path = Path(__file__).parent.parent / "data/inputs/day_4/input.txt"

text = input_path.read_text()
lines = text.split("\n")
array = np.array([list(line) for line in lines if line])


def belongs_to_xmas(a: np.ndarray, i: int, j: int) -> bool:
    all_words_of_7_letters = [
        a[i - 3, j]
        + a[i - 2, j]
        + a[i - 1, j]
        + a[i, j]
        + a[i + 1, j]
        + a[i + 2, j]
        + a[i + 3, j],
        a[i, j - 3]
        + a[i, j - 2]
        + a[i, j - 1]
        + a[i, j]
        + a[i, j + 1]
        + a[i, j + 2]
        + a[i, j + 3],
        a[i - 3, j - 3],
        a[i - 2, j - 2]
        + a[i - 1, j - 1]
        + a[i, j]
        + a[i + 1, j + 1]
        + a[i + 2, j + 2]
        + a[i + 3, j + 3],
        a[i - 3, j + 3],
        a[i - 2, j + 2]
        + a[i - 1, j + 1]
        + a[i, j]
        + a[i + 1, j - 1]
        + a[i + 2, j - 2]
        + a[i + 3, j - 3],
    ]
    for word in all_words_of_7_letters:
        if "XMAS" in word or "XMAS" in word[::-1]:
            return True
    return False


for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if not belongs_to_xmas(array, i, j):
            array[i, j] = "."

print(array)
