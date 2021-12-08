import matplotlib.pyplot as plt
import networkx as nx
import os
import re

BAG_NAME = r'[a-z]+ [a-z]+'
BAG = r'(\d+ %s) bags?(?:\.|, )' % BAG_NAME
CONTAINER = r'^(%s)' % BAG_NAME

MY_BAG = 'shiny gold'


def extract(rule):
    container = re.search(CONTAINER, rule).group()
    bags = re.findall(BAG, rule)

    # map each bag "X name" to (X, "name")
    for i, bag in enumerate(bags):
        amount, name = bag.split(' ', 1)
        amount = int(amount)
        bags[i] = (amount, name)

    return (container, bags)


def amount_of_bags(container, graph, first_call=True):
    bags = [(bag, graph[container][bag]['amount'])
            for bag in graph.successors(container)]

    if not bags:
        return 1

    amount = 0

    for bag, n in bags:
        amount += n * amount_of_bags(bag, graph, first_call=False)

    if first_call:
        return amount

    return amount + 1


def build_graph(rules):
    g = nx.DiGraph()

    for rule in rules:
        container, bags = extract(rule)

        for amount, bag in bags:
            g.add_edge(container, bag, amount=amount)

    return g


def count(rules):
    g = build_graph(rules)
    return amount_of_bags(MY_BAG, g)


def main():
    with open(os.getcwd() + '/input.txt') as f:
        rules = [line.strip() for line in f.readlines()]

    print(count(rules))


if __name__ == "__main__":
    main()