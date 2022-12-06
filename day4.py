def part1():
    with open('inputs/day4.txt') as f:
        total = 0
        for line in f.readlines():
            first_interval, second_interval = line.strip().split(",")
            first_start, first_end = [int(v) for v in first_interval.split("-")]
            second_start, second_end = [int(v) for v in second_interval.split("-")]

            if (first_start >= second_start and first_end <= second_end) \
                    or (second_start >= first_start and second_end <= first_end):
                total += 1
        print(total)


def part2():
    with open('inputs/day4.txt') as f:
        total = 0
        for line in f.readlines():
            first_interval, second_interval = line.strip().split(",")
            first_start, first_end = [int(v) for v in first_interval.split("-")]
            second_start, second_end = [int(v) for v in second_interval.split("-")]

            if second_start <= first_start <= second_end or first_start <= second_start <= first_end:
                total += 1
        print(total)


if __name__ == "__main__":
    part1()
    part2()