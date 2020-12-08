"""
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
                    weight=int(item_tokens[0])
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
