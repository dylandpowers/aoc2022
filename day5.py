from collections import deque


def part1():
    with open('inputs/day5.txt') as f:
        stacks = []

        # There are always just 9 stacks
        for i in range(9):
            stacks.append(deque())

        finished_reading_stacks = False
        for line in f.readlines():
            if line == '\n':
                finished_reading_stacks = True
                continue

            if not finished_reading_stacks:
                if line[0] == '1':
                    # This is the line for the numbered stacks
                    continue
                for i in range(0, len(line) - 1, 4):
                    if line[i] == ' ':
                        # no crate at this position
                        continue
                    stacks[i // 4].appendleft(line[i + 1])
            else:
                # These are the movement procedure lines
                num_to_move = int(line[5:line.index(' ', 5)])
                from_index = line.index('from')
                origin_stack = int(line[from_index + 5])
                dest_stack = int(line[from_index + 10])

                for i in range(num_to_move):
                    stacks[dest_stack - 1].append(stacks[origin_stack - 1].pop())

        print(''.join([stack[-1] for stack in stacks]))


def part2():
    with open('inputs/day5.txt') as f:
        stacks = []

        # There are always just 9 stacks
        for i in range(9):
            stacks.append(deque())

        finished_reading_stacks = False
        for line in f.readlines():
            if line == '\n':
                finished_reading_stacks = True
                continue

            if not finished_reading_stacks:
                if line[0] == '1':
                    # This is the line for the numbered stacks
                    continue
                for i in range(0, len(line) - 1, 4):
                    if line[i] == ' ':
                        # no crate at this position
                        continue
                    stacks[i // 4].appendleft(line[i + 1])
            else:
                # These are the movement procedure lines
                num_to_move = int(line[5:line.index(' ', 5)])
                from_index = line.index('from')
                origin_stack = int(line[from_index + 5])
                dest_stack = int(line[from_index + 10])

                temp = []
                for i in range(num_to_move):
                    temp.append(stacks[origin_stack - 1].pop())

                while len(temp) > 0:
                    stacks[dest_stack - 1].append(temp.pop())

        print(''.join([stack[-1] for stack in stacks]))


if __name__ == "__main__":
    # part1()
    part2()
