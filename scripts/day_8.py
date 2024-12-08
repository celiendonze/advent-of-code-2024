from collections import defaultdict
from itertools import combinations, product
from pathlib import Path

import numpy as np
from tqdm import tqdm

day_8_input = Path("data/inputs/day_8/input.txt").read_text().strip().split("\n")
# day_8_input = (
#     """
# ......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.
# """.replace("#", ".")
#     .strip()
#     .split("\n")
# )

matrix = np.array([list(x) for x in day_8_input])


positions = defaultdict(list)

for i, j in product(range(matrix.shape[0]), range(matrix.shape[1])):
    value = matrix[i, j]
    if value != ".":
        positions[str(value)].append((i, j))

antinodes_matrix = np.zeros_like(matrix)
antinodes_matrix.fill(".")


def is_inside_matrix(pos: tuple[int, int], matrix: np.ndarray):
    x, y = pos
    return all(
        [
            x >= 0,
            y >= 0,
            x < matrix.shape[0],
            y < matrix.shape[1],
        ]
    )


for key, pos in tqdm(positions.items()):
    if len(pos) < 2:
        continue
    for combi in combinations(pos, 2):
        a, b = np.array(combi)
        vec1 = a - b
        vec2 = b - a
        antinode_a = a + vec1
        antinode_b = b + vec2

        if is_inside_matrix(antinode_a, antinodes_matrix):
            antinodes_matrix[antinode_a[0], antinode_a[1]] = "#"
        if is_inside_matrix(antinode_b, antinodes_matrix):
            antinodes_matrix[antinode_b[0], antinode_b[1]] = "#"

print("Part 1:")
print(np.count_nonzero(antinodes_matrix == "#"))

# Part 2:
antinodes_matrix = np.zeros_like(matrix)
antinodes_matrix.fill(".")

for key, pos in tqdm(positions.items()):
    if len(pos) < 2:
        continue
    for combi in combinations(pos, 2):
        a, b = np.array(combi)
        antinodes_matrix[a[0], a[1]] = "#"
        antinodes_matrix[b[0], b[1]] = "#"
        vec1 = a - b
        vec2 = b - a
        antinode_a = a + vec1
        antinode_b = b + vec2

        while is_inside_matrix(antinode_a, antinodes_matrix) or is_inside_matrix(
            antinode_b, antinodes_matrix
        ):
            if is_inside_matrix(antinode_a, antinodes_matrix):
                antinodes_matrix[antinode_a[0], antinode_a[1]] = "#"

            if is_inside_matrix(antinode_b, antinodes_matrix):
                antinodes_matrix[antinode_b[0], antinode_b[1]] = "#"
            antinode_a += vec1
            antinode_b += vec2

print("Part 2:")
print(np.count_nonzero(antinodes_matrix == "#"))

# for row in antinodes_matrix:
#     print("".join(row))
