from itertools import product
from pathlib import Path

import numpy as np
from tqdm import tqdm

day_20_input = Path("data/inputs/day_20/input.txt").read_text().strip()
# day_20_input = """
# ###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# """.strip()


labyrinth = np.array([list(r) for r in day_20_input.split("\n")])
EMPTY_CHAR = "."
WALL_CHAR = "#"
START_CHAR = "S"
END_CHAR = "E"


def find_shortest_path(labyrinth: np.ndarray) -> int:
    """Find the shortest path with A* algorithm.

    Args:
        labyrinth (list[str]): The labyrinth represented as a list of strings.

    Returns:
        int: Length of the shortest path from start to end.
    """

    start_position = tuple(np.argwhere(labyrinth == START_CHAR)[0])
    end_position = tuple(np.argwhere(labyrinth == END_CHAR)[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbours(position):
        neighbours = []
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbour = (position[0] + i, position[1] + j)
            if (
                0 <= neighbour[0] < labyrinth.shape[0]
                and 0 <= neighbour[1] < labyrinth.shape[1]
            ):
                if labyrinth[neighbour] != WALL_CHAR:
                    neighbours.append(neighbour)
        return neighbours

    open_set = {start_position}
    came_from = {}
    g_score = {start_position: 0}
    f_score = {start_position: heuristic(start_position, end_position)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end_position:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return len(path)

        open_set.remove(current)
        for neighbour in get_neighbours(current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbour, float("inf")):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(
                    neighbour, end_position
                )
                if neighbour not in open_set:
                    open_set.add(neighbour)


# print(labyrinth)
print(find_shortest_path(labyrinth))

count = 0
original_shortest_path = find_shortest_path(labyrinth)
for i, j in tqdm(
    product(range(labyrinth.shape[0]), range(labyrinth.shape[1])), total=labyrinth.size
):
    if labyrinth[i, j] == WALL_CHAR:
        labyrinth[i, j] = "."
        new_shortest_path = find_shortest_path(labyrinth)
        if original_shortest_path - new_shortest_path >= 100:
            count += 1
        labyrinth[i, j] = "#"

print("Part 1:")
print(count)
