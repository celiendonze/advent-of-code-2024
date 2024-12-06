from pathlib import Path

import numpy as np

day_6_input = Path("data/inputs/day_6/input.txt").read_text().strip().split("\n")

# day_6_input = """
# ..#..
# .....
# #.^.#
# .....
# ..#..
# """.strip().split("\n")

world_map = np.array([list(c) for c in day_6_input])


def is_outside(pos):
    return (
        pos[0] < 0
        or pos[0] >= world_map.shape[0]
        or pos[1] < 0
        or pos[1] >= world_map.shape[1]
    )


# left to right, clockwise
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

visited = set()

for i in range(world_map.shape[0]):
    for j in range(world_map.shape[1]):
        if world_map[i, j] not in ".#udlr":
            current_pos = np.array([i, j])
            break

# print(current_pos, world_map[tuple(current_pos)])
visited.add(tuple(current_pos))
current_direction = directions[0]
while True:
    next_pos = current_pos + np.array(current_direction)
    if is_outside(next_pos):
        break
    next_coords = tuple(next_pos)
    next_char = world_map[next_coords]

    while next_char == "#":
        current_direction = directions[(directions.index(current_direction) + 1) % 4]
        next_pos = current_pos + np.array(current_direction)
        next_coords = tuple(next_pos)
        next_char = world_map[next_coords]
        # print("changing direction to", current_direction)
    # print(next_char)
    current_pos = next_pos
    visited.add(next_coords)

print(len(visited))
