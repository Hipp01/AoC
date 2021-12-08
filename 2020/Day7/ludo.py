import matplotlib.pyplot as plt
import networkx as nx
import os
import re

BAG_NAME = '[a-z]+ [a-z]+'
BAG = f'\d+ ({BAG_NAME}) bags?(?:\.|, )'
CONTAINER = f'^({BAG_NAME})'

MY_BAG = 'shiny gold'


def extract(rule):
    container = re.search(CONTAINER, rule).group()
    bags = re.findall(BAG, rule)
    return (container, bags)


def count(rules):
    g = nx.DiGraph()

    for rule in rules:
        container, bags = extract(rule)

        for bag in bags:
            g.add_edge(container, bag)

    queue = [MY_BAG]
    counter = 0
    visited = set()

    while queue:
        node = queue.pop()
        containers = g.predecessors(node)

        for container in containers:
            if container not in visited:
                visited.add(container)
                queue.append(container)
                counter += 1

    return counter


def main():
    with open(os.getcwd() + '/input.txt') as f:
        rules = [line.strip() for line in f.readlines()]

    print(count(rules))


if __name__ == "__main__":
    main()