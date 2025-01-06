import re
from itertools import product
from pathlib import Path

import numpy as np
from tqdm import tqdm

day_13_input = Path("data/inputs/day_13/input.txt").read_text().strip()
prizes = day_13_input.split("\n\n")

COST_TO_PRESS_A = 3
COST_TO_PRESS_B = 1

pattern_to_find_button_A = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
pattern_to_find_button_B = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
pattern_to_find_prize_location = re.compile(r"Prize: X=(\d+), Y=(\d+)")


def solve_claw_machine(button_A, button_B, target):
    button_A = np.array(button_A, dtype=int)
    button_B = np.array(button_B, dtype=int)
    target = np.array(target, dtype=int)

    def f(x, y):
        return np.linalg.norm(x * button_A + y * button_B - target)

    for x in range(100, 0, -1):
        for y in range(100):
            if np.linalg.norm(x * button_A + y * button_B) > np.linalg.norm(target):
                break
            if f(x, y) == 0:
                return [(x, y)]
    return []


total_cost = 0
for prize_str in tqdm(prizes):
    # print(prize_str)
    button_A = re.findall(pattern_to_find_button_A, prize_str)[0]
    button_B = re.findall(pattern_to_find_button_B, prize_str)[0]
    target = re.findall(pattern_to_find_prize_location, prize_str)[0]

    solutions = solve_claw_machine(button_A, button_B, target)
    if solutions:
        min_cost_solution = min(
            solutions, key=lambda x: COST_TO_PRESS_A * x[0] + COST_TO_PRESS_B * x[1]
        )
        total_cost += (
            COST_TO_PRESS_A * min_cost_solution[0]
            + COST_TO_PRESS_B * min_cost_solution[1]
        )

print("Part 1:")
print(total_cost)  # 37680

print("Part 2:")
total_cost = 0
# TODO
print(total_cost)
