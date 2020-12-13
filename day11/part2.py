"""
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


def solve_part2(room_state: list) -> int:
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
    elif state[row][col] == "#" and adjacent_occupied >= 5:
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

    adjacent_occupied = []
    for coordinate in adjacent_deltas:
        drow, dcol = coordinate

        nrow = row + drow
        ncol = col + dcol

        seat = None
        while (nrow >= 0 and nrow < len(state)) and (
            ncol >= 0 and ncol < len(state[nrow])
        ):
            seat = state[nrow][ncol]

            if seat != ".":
                break

            nrow += drow
            ncol += dcol

        adjacent_occupied.append(seat)

    count = 0
    for seat in adjacent_occupied:
        if seat and seat == "#":
            count += 1

    return count


def main():
    with open("input.txt") as f:
        room_state = [list(line.replace("\n", "")) for line in f]

    part2 = solve_part2(room_state=room_state)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
