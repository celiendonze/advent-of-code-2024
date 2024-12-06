from collections import defaultdict
from pathlib import Path

import networkx as nx
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


def is_page_valid(page: list[int]) -> bool:
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
print(s)  # 5248


def sort_page(page: list[int]) -> list[int]:
    graph = nx.DiGraph()
    for k, v in rules.items():
        for e in v:
            if k in page and e in page:
                graph.add_edge(k, e)
    sorted_page = list(nx.topological_sort(graph))
    return sorted_page


second_sum = 0
for page in tqdm(unordered_pages):
    page = sort_page(page)
    second_sum += page[len(page) // 2]


print("part 2:")
print(second_sum)  # 4507
