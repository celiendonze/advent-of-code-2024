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

for key, pos in tqdm(positions.items()):
    if len(pos) < 2:
        continue
    for combi in combinations(pos, 2):
        a, b = np.array(combi)
        vec1 = a - b
        vec2 = b - a
        antinode_a = a + vec1
        antinode_b = b + vec2

        if all(
            [
                antinode_a[0] >= 0,
                antinode_a[1] >= 0,
                antinode_a[0] < matrix.shape[0],
                antinode_a[1] < matrix.shape[1],
            ]
        ):
            # if matrix[antinode_a[0], antinode_a[1]] == ".":
            #     matrix[antinode_a[0], antinode_a[1]] = "#"
            antinodes_matrix[antinode_a[0], antinode_a[1]] = "#"
        if all(
            [
                antinode_b[0] >= 0,
                antinode_b[1] >= 0,
                antinode_b[0] < matrix.shape[0],
                antinode_b[1] < matrix.shape[1],
            ]
        ):
            # if matrix[antinode_b[0], antinode_b[1]] == ".":
            #     matrix[antinode_b[0], antinode_b[1]] = "#"
            antinodes_matrix[antinode_b[0], antinode_b[1]] = "#"

print("Part 1:")
print(np.count_nonzero(antinodes_matrix == "#"))

# solution = """
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
# """.strip().split("\n")

# for i, row in enumerate(matrix):
#     print("".join(row), solution[i])

# Part 2:
antinodes_matrix = np.zeros_like(matrix)
antinodes_matrix.fill(".")

for key, pos in tqdm(positions.items()):
    if len(pos) < 2:
        continue
    for combi in combinations(pos, 2):
        a, b = np.array(combi)
        vec1 = a - b
        vec2 = b - a
        antinode_a = a + vec1
        antinode_b = b + vec2

        while all(
            [
                antinode_a[0] >= 0,
                antinode_a[1] >= 0,
                antinode_a[0] < matrix.shape[0],
                antinode_a[1] < matrix.shape[1],
            ]
        ) or all(
            [
                antinode_b[0] >= 0,
                antinode_b[1] >= 0,
                antinode_b[0] < matrix.shape[0],
                antinode_b[1] < matrix.shape[1],
            ]
        ):
            if all(
                [
                    antinode_a[0] >= 0,
                    antinode_a[1] >= 0,
                    antinode_a[0] < matrix.shape[0],
                    antinode_a[1] < matrix.shape[1],
                ]
            ):
                # if matrix[antinode_a[0], antinode_a[1]] == ".":
                #     matrix[antinode_a[0], antinode_a[1]] = "#"
                antinodes_matrix[antinode_a[0], antinode_a[1]] = "#"
            if all(
                [
                    antinode_b[0] >= 0,
                    antinode_b[1] >= 0,
                    antinode_b[0] < matrix.shape[0],
                    antinode_b[1] < matrix.shape[1],
                ]
            ):
                # if matrix[antinode_b[0], antinode_b[1]] == ".":
                #     matrix[antinode_b[0], antinode_b[1]] = "#"
                antinodes_matrix[antinode_b[0], antinode_b[1]] = "#"
            antinode_a += vec1
            antinode_b += vec2

print("Part 2:")
print(np.count_nonzero(antinodes_matrix == "#"))
