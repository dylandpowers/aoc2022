from queue import PriorityQueue


def part1():
    with open("inputs/day1.txt") as f:
        elves = []
        curr_total = 0
        for line in f.readlines():
            if line == '\n':
                elves.append(curr_total)
                curr_total = 0
            else:
                curr_total += int(line)
    print(max(elves))


def part2():
    with open("inputs/day1.txt") as f:
        q = PriorityQueue()
        curr_total = 0
        for line in f.readlines():
            if line == '\n':
                q.put(curr_total)
                if q.qsize() > 3:
                    q.get()
                curr_total = 0
            else:
                curr_total += int(line)

        top3 = 0
        while not q.empty():
            top3 += q.get()
        print(top3)


if __name__ == "__main__":
    # part1()
    part2()
