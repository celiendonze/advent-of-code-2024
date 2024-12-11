from itertools import product
from pathlib import Path

import numpy as np

day_10_input = Path("data/inputs/day_10/input.txt").read_text().strip().split("\n")
# day_10_input = """
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """.strip().split("\n")
array = np.array([list(i) for i in day_10_input], dtype=int)

print(array)


def find_number_of_path_to_9(start_position, array) -> int:
    current_num = array[start_position]
    if current_num == 9:
        return 1
    next_positions = []
    # Check around the current position (left, right, up, down)
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_position = (start_position[0] + i, start_position[1] + j)
        if (
            0 <= new_position[0] < array.shape[0]
            and 0 <= new_position[1] < array.shape[1]
        ):
            if array[new_position] == current_num + 1:
                next_positions.append(new_position)

    if len(next_positions) == 0:
        return 0

    return sum(find_number_of_path_to_9(pos, array) for pos in next_positions)


def find_number_all_9_reachable(start_position, array) -> set[tuple[int, int]]:
    current_num = array[start_position]
    if current_num == 9:
        return {start_position}
    next_positions = []
    # Check around the current position (left, right, up, down)
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_position = (start_position[0] + i, start_position[1] + j)
        if (
            0 <= new_position[0] < array.shape[0]
            and 0 <= new_position[1] < array.shape[1]
        ):
            if array[new_position] == current_num + 1:
                next_positions.append(new_position)

    if len(next_positions) == 0:
        return set()

    return set.union(
        *(find_number_all_9_reachable(pos, array) for pos in next_positions)
    )


paths = []
for i, j in product(range(array.shape[0]), range(array.shape[1])):
    if array[i, j] == 0:
        # number_of_paths = find_number_of_path_to_9((i, j), array)
        # paths.append(number_of_paths)
        # print(f"Number of paths from {i, j} to 9: {number_of_paths}")
        all_9_reachable = find_number_all_9_reachable((i, j), array)
        # print(f"All 9 reachable from {i, j}: {all_9_reachable}")
        paths.append(len(all_9_reachable))

print("Part 1:")
print(sum(paths))

# Part 2
paths = []
for i, j in product(range(array.shape[0]), range(array.shape[1])):
    if array[i, j] == 0:
        paths_to_9 = find_number_of_path_to_9((i, j), array)
        paths.append(paths_to_9)

print("Part 2:")
print(sum(paths))
