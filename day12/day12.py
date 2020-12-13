"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster
than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather
than giving a route directly to safety, it produced extremely circuitous instructions.
When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character
actions paired with integer input values. After staring at them for a few minutes, you
work out what they probably mean:

    - Action N means to move north by the given value.
    - Action S means to move south by the given value.
    - Action E means to move east by the given value.
    - Action W means to move west by the given value.
    - Action L means to turn left the given number of degrees.
    - Action R means to turn right the given number of degrees.
    - Action F means to move forward by the given value in the
      direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the
ship is facing. (That is, if the ship is facing east and the next instruction is N10, 
the ship would move north 10 units, but would still move east if the following action
were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    - F10 would move the ship 10 units east (because the ship starts by facing east)
      to east 10, north 0.
    - N3 would move the ship 3 units north to east 10, north 3.
    - F7 would move the ship another 7 units east (because the ship is still facing
      east) to east 17, north 3.
    - R90 would cause the ship to turn right by 90 degrees and face south; it remains
      at east 17, north 3.
    - F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute
values of its east/west position and its north/south position) from its starting
position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between
that location and the ship's starting position?

--- Part Two ---

Before you can give the destination to the captain, you realize that the actual action
meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the
ship's position:


    - Action N means to move the waypoint north by the given value.
    - Action S means to move the waypoint south by the given value.
    - Action E means to move the waypoint east by the given value.
    - Action W means to move the waypoint west by the given value.
    - Action L means to rotate the waypoint around the ship left
      (counter-clockwise) the given number of degrees.
    - Action R means to rotate the waypoint around the ship right
      (clockwise) the given number of degrees.
    - Action F means to move forward to the waypoint a number of times
      equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint
is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

    - F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10
      units north), leaving the ship at east 100, north 10. The waypoint stays 10 units
      east and 1 unit north of the ship.
    - N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship.
      The ship remains at east 100, north 10.
    - F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north),
      leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units
      north of the ship.
    - R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east 
      and 10 units south of the ship. The ship remains at east 170, north 38.
    - F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south),
      leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units
      south of the ship.

After these operations, the ship's Manhattan distance from its starting position is
214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan
distance between that location and the ship's starting position?

"""

import re


def turn_left(direction: str) -> str:
    if direction == "N":
        return "W"
    elif direction == "S":
        return "E"
    elif direction == "E":
        return "N"
    elif direction == "W":
        return "S"
    else:
        raise Exception("Unknown direction")


def turn_right(direction: str) -> str:
    if direction == "N":
        return "E"
    elif direction == "S":
        return "W"
    elif direction == "E":
        return "S"
    elif direction == "W":
        return "N"
    else:
        raise Exception("Unknown direction")


def solve_part1(rules: list) -> int:
    position = [0, 0]
    current_dir = "E"

    for rule in rules:
        action, value = rule

        if action == "N":
            position[1] -= value
        elif action == "S":
            position[1] += value
        elif action == "E":
            position[0] += value
        elif action == "W":
            position[0] -= value
        elif action == "L":
            for _ in range(int(value / 90)):
                current_dir = turn_left(current_dir)
        elif action == "R":
            for _ in range(int(value / 90)):
                current_dir = turn_right(current_dir)
        elif action == "F":
            if current_dir == "N":
                position[1] -= value
            elif current_dir == "S":
                position[1] += value
            elif current_dir == "E":
                position[0] += value
            elif current_dir == "W":
                position[0] -= value
            else:
                raise Exception("Unknown direction encountered")
        else:
            raise Exception("Unknown direction encountered")

    return abs(position[0]) + abs(position[1])


def rotate_left(point: list) -> list:
    return [point[1], -1 * point[0]]


def rotate_right(point: list) -> list:
    return [-1 * point[1], point[0]]


def solve_part2(rules: list) -> int:
    position = [0, 0]
    waypoint = [10, -1]

    for rule in rules:
        action, value = rule

        if action == "N":
            waypoint[1] -= value
        elif action == "S":
            waypoint[1] += value
        elif action == "E":
            waypoint[0] += value
        elif action == "W":
            waypoint[0] -= value
        elif action == "R":
            for _ in range(int(value / 90)):
                waypoint = rotate_right(waypoint)
        elif action == "L":
            for _ in range(int(value / 90)):
                waypoint = rotate_left(waypoint)
        elif action == "F":
            position[0] += waypoint[0] * value
            position[1] += waypoint[1] * value
        else:
            raise Exception("Unknown direction encountered")

    return abs(position[0]) + abs(position[1])


def main():
    with open("input.txt") as f:
        instructions = [line for line in f]

    nav_rules = []
    for instruction in instructions:
        match = re.match(r"(?P<action>\w{1})(?P<value>\d+)", instruction)
        nav_rules.append([match.group("action"), int(match.group("value"))])

    part1 = solve_part1(rules=nav_rules)
    part2 = solve_part2(rules=nav_rules)

    print(f"part1: {part1}")
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
