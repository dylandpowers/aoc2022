MOVES = {
    'A': 'R',
    'X': 'R',
    'B': 'P',
    'Y': 'P',
    'C': 'S',
    'Z': 'S'
}


POINTS = {
    'R': 1,
    'P': 2,
    'S': 3
}


OUTCOMES = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}


def part1():
    """
    A, X: rock (1 point)
    B, Y: paper (2 points)
    C, Z: scissors (3 points)
    """
    with open('inputs/day2.txt') as f:
        total = 0
        for line in f.readlines():
            their_move_raw, our_move_raw = line.strip().split()
            their_move = MOVES[their_move_raw]
            our_move = MOVES[our_move_raw]

            if our_move == their_move:
                total += 3 + POINTS[our_move]
            elif OUTCOMES[their_move] == our_move:
                total += POINTS[our_move]
            else:
                total += 6 + POINTS[our_move]

        print(total)


def part2():
    """
    X: lose
    Y: draw
    Z: win
    """
    with open('inputs/day2.txt') as f:
        total = 0
        outcomes_reversed = { v: k for k, v in OUTCOMES.items() }
        for line in f.readlines():
            their_move_raw, desired_outcome = line.strip().split()
            their_move = MOVES[their_move_raw]

            if desired_outcome == 'X':
                total += POINTS[OUTCOMES[their_move]]
            elif desired_outcome == 'Y':
                total += 3 + POINTS[their_move]
            else:
                total += 6 + POINTS[outcomes_reversed[their_move]]

        print(total)


if __name__ == "__main__":
    # part1()
    part2()