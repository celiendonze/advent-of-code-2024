from collections import defaultdict
from itertools import permutations
from pathlib import Path

# from random import shuffle
from tqdm.auto import tqdm

day_5_input = Path("data/inputs/day_5/input.txt").read_text().strip().split("\n")

rules = defaultdict(list)
pages = []

for line in day_5_input:
    if not line:
        continue
    if "|" in line:
        rule = line.split("|")
        rules[int(rule[0])].append(int(rule[1]))
    else:
        pages.append([int(e) for e in line.split(",")])


def is_page_valid(page):
    for i, e in enumerate(page[::-1]):
        if e in rules:
            must_be_after = rules[e]
            if any([b in must_be_after for b in page[: len(page) - i - 1]]):
                return False
    return True


unordered_pages = []
s = 0
for page in pages:
    is_valid = is_page_valid(page)
    if not is_valid:
        unordered_pages.append(page)
    if is_valid:
        s += page[len(page) // 2]  # middle element

print("part 1:")
print(s)


def sort_page(page):
    sorted_page = []

    return sorted_page


second_sum = 0
for page in tqdm(unordered_pages):
    for perm in tqdm(list(permutations(page))):
        if is_page_valid(perm):
            second_sum += perm[len(perm) // 2]
            break

print("part 2:")
print(second_sum)
