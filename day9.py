def part1():
    with open('inputs/day9.txt') as f:
        insns = [tuple(line.strip().split()) for line in f.readlines()]

    head_row = 0
    head_col = 0
    tail_row = 0
    tail_col = 0

    visited = set()
    for insn in insns:
        dir = insn[0]
        units = int(insn[1])

        for _ in range(units):
            # the previous head position is where the tail will be next
            prev = (head_row, head_col)
            if dir == 'U':
                head_row -= 1
            elif dir == 'D':
                head_row += 1
            elif dir == 'L':
                head_col -= 1
            else:
                head_col += 1

            if abs(head_row - tail_row) > 1 or abs(head_col - tail_col) > 1:
                tail_row, tail_col = prev

            visited.add((tail_row, tail_col))

    print(len(visited))


def part2():
    with open('inputs/day9.txt') as f:
        insns = [tuple(line.strip().split()) for line in f.readlines()]

    visited = set()
    head_row = 0
    head_col = 0
    positions = [(0, 0)] * 9

    for insn in insns:
        dir = insn[0]
        units = int(insn[1])

        for _ in range(units):
            prev = (head_row, head_col)
            if dir == 'U':
                head_row -= 1
            elif dir == 'D':
                head_row += 1
            elif dir == 'L':
                head_col -= 1
            else:
                head_col += 1

            # Update the positions of the rest of the knots
            updated_row = head_row
            updated_col = head_col
            for i in range(len(positions)):
                row, col = positions[i]
                # if the difference is big enough, we need to update the current position to the
                # previous position of the knot before it
                if abs(updated_row - row) > 1 or abs(updated_col - col) > 1:
                    # the current position will move to prev
                    positions[i] = prev

                updated_row, updated_col = positions[i]
                prev = (row, col)

            visited.add(positions[-1])

    print(len(visited))


if __name__ == "__main__":
    part1()
    part2()