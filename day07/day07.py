"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact,
it looks like you'll even have time to grab some food: all flights are
currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are
being enforced about bags and their contents; bags must be color-coded and
must contain specific quantities of other color-coded bags. Apparently,
nobody responsible for these regulations considered how long they would
take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example,
every faded blue bag is empty, every vibrant plum bag contains 11 bags (5
faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag,
how many different bag colors would be valid for the outermost bag? (In other
words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    - A bright white bag, which can hold your shiny gold bag directly.
    - A muted yellow bag, which can hold your shiny gold bag directly, plus
      some other bags.
    - A dark orange bag, which can hold bright white and muted yellow bags,
      either of which could then hold your shiny gold bag.
    - A light red bag, which can hold bright white and muted yellow bags, either
      of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one
shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules
is quite long; make sure you get all of it.)

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices,
but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    - faded blue bags contain 0 other bags.
    - dotted black bags contain 0 other bags.
    - vibrant plum bags contain 11 other bags: 5 faded blue bags and
      6 dotted black bags.
    - dark olive bags contain 7 other bags: 3 faded blue bags and 4
      dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it)
plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper
than this example; be sure to count all of the bags, even if the nesting becomes
topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

"""


class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    def add_adjacent(self, other, weight):
        self.adjacent[other] = weight

    def get_parents(self):
        parents = {}
        for i in self.adjacent.keys():
            if self.adjacent[i] < 0:
                parents[i] = self.adjacent[i]
        return parents

    def get_children(self):
        children = {}
        for i in self.adjacent.keys():
            if self.adjacent[i] > 0:
                children[i] = self.adjacent[i]
        return children

    def get_edge(self, other):
        return self.adjacent[other]

    def __str__(self):
        return f"{self.id}: {self.adjacent}"


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        if id not in self.nodes.keys():
            self.nodes[id] = Node(id)

    def get_node(self, id):
        return self.nodes[id] if id in self.nodes.keys() else None

    def add_edge(self, parent, child, weight):
        weight = abs(weight)
        if parent not in self.nodes.keys():
            self.add_node(parent)
        if child not in self.nodes.keys():
            self.add_node(child)

        self.nodes[parent].add_adjacent(child, weight)
        self.nodes[child].add_adjacent(parent, 0 - weight)


def read_rules():
    rules = Graph()
    with open("input.txt") as f:
        for line in f.read().splitlines():
            key, contents = line.split("bags contain ")
            rules.add_node(key.strip())
            if "no other" in line:
                continue
            content_list = contents.split(", ")
            for item in content_list:
                item_tokens = item.split()
                rules.add_edge(
                    parent=key.strip(),
                    child=" ".join(item_tokens[1:-1]).strip(),
                    weight=int(item_tokens[0]),
                )
    return rules


def solve_part1(rules: Graph) -> int:
    valid = set()
    start = rules.get_node("shiny gold")
    to_process = set(start.get_parents().keys())
    while len(to_process) != 0:
        curr = to_process.pop()
        to_process.update(rules.get_node(curr).get_parents().keys())
        valid.add(curr)
    return len(valid)


def get_num_bags(rules, id):
    node = rules.get_node(id)
    children = node.get_children()
    if len(children) == 0:
        return 1
    else:
        return 1 + sum([children[i] * get_num_bags(rules, i) for i in children])


def solve_part2(rules: Graph) -> int:
    return get_num_bags(rules, "shiny gold") - 1


def main():
    rules = read_rules()

    part1 = solve_part1(rules=rules)
    part2 = solve_part2(rules=rules)

    print(f"part1: {part1}")
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
