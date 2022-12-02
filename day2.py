OUTCOMES = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3
}

POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


MATCH_POINTS = {
    'X': 0,
    'Y': 3,
    'Z': 6
}


POINTS_FOR_MOVE = {
    ('A', 'X'): 3,
    ('A', 'Y'): 1,
    ('A', 'Z'): 2,
    ('B', 'X'): 1,
    ('B', 'Y'): 2,
    ('B', 'Z'): 3,
    ('C', 'X'): 2,
    ('C', 'Y'): 3,
    ('C', 'Z'): 1
}


def part1():
    """
    A, X: rock (1 point)
    B, Y: paper (2 points)
    C, Z: scissors (3 points)
    """
    with open('inputs/day2.txt') as f:
        moves = [tuple(s.strip().split(" ")) for s in f.readlines()]

    print(sum([OUTCOMES[play] + POINTS[play[1]] for play in moves]))


def part2():
    """
    X: lose
    Y: draw
    Z: win
    """
    with open('inputs/day2.txt') as f:
        moves = [tuple(s.strip().split(" ")) for s in f.readlines()]

    print(sum([POINTS_FOR_MOVE[play] + MATCH_POINTS[play[1]] for play in moves]))


if __name__ == "__main__":
    #part1()
    part2()