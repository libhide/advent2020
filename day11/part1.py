"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey
is a ferry that goes directly to the tropical island where you can finally start
your vacation. As you reach the waiting area to board the ferry, you realize you're
so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting
area, you're pretty sure you can predict the best place to sit. You make a quick map
of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat
(L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people
are entirely predictable and always follow a simple set of rules. All decisions are based
on the number of occupied seats adjacent to a given seat (one of the eight positions immediately
up, down, left, right, or diagonal from the seat). The following rules are applied
to every seat simultaneously:

    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    - Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications
of these rules cause no seats to change state! Once people stop moving around, you count
37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state.
How many seats end up occupied?
"""

from copy import deepcopy


def display_seating(seating_arrangement: list):
    print("\n", end="")
    for i in range(len(seating_arrangement)):
        for j in range(len(seating_arrangement[i])):
            print(seating_arrangement[i][j], end="")
            if j == len(seating_arrangement[i]) - 1:
                print("\n", end="")
    print("\n", end="")


def solve_part1(room_state: list) -> int:
    return chaos(room_state)


def chaos(original_state):
    state = deepcopy(original_state)
    changed = True

    while changed:
        state, changed = iterate(state)

    count = 0
    for row in state:
        for col in row:
            if col == "#":
                count += 1

    return count


def iterate(original_state) -> tuple:
    next_state = deepcopy(original_state)

    changed = False
    for row, line in enumerate(original_state):
        for col, seat in enumerate(line):
            new_seat_state = apply_rules(original_state, row, col)
            if new_seat_state != original_state[row][col]:
                changed = True
            next_state[row][col] = new_seat_state

    return (next_state, changed)


def apply_rules(state, row, col) -> str:
    if state[row][col] == ".":
        return "."

    adjacent_occupied = count_adjacent(state, row, col)

    if state[row][col] == "L" and adjacent_occupied == 0:
        return "#"
    elif state[row][col] == "#" and adjacent_occupied >= 4:
        return "L"
    else:
        return state[row][col]


def count_adjacent(state, row, col) -> int:
    adjacent_deltas = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]

    adjacent_positions = []
    for coordinate in adjacent_deltas:
        drow, dcol = coordinate
        adjacent_positions.append([row + drow, col + dcol])

    filtered_adjacent_positions = []
    for coordinate in adjacent_positions:
        nrow, ncol = coordinate
        if (nrow >= 0 and nrow < len(state)) and (
            ncol >= 0 and ncol < len(state[nrow])
        ):
            filtered_adjacent_positions.append(coordinate)

    occupied_count = 0
    for coordinate in filtered_adjacent_positions:
        row, col = coordinate
        if state[row][col] == "#":
            occupied_count += 1

    return occupied_count


def solve_part2(seating_arrangement: list) -> int:
    pass


def main():
    with open("input.txt") as f:
        room_state = [list(line.replace("\n", "")) for line in f]

    part1 = solve_part1(room_state=room_state)
    print(f"part1: {part1}")


if __name__ == "__main__":
    main()
