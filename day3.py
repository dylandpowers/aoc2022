def part1():
    total = 0
    with open('inputs/day3.txt') as f:
        for line in f.readlines():
            items = line.strip()
            first_compartment = set(items[:len(items) // 2])
            second_compartment = set(items[len(items) // 2:])

            duplicate_item = first_compartment.intersection(second_compartment).pop()

            if duplicate_item.isupper():
                total += ord(duplicate_item) - ord('A') + 27
            else:
                total += ord(duplicate_item) - ord('a') + 1

    print(total)


def part2():
    total = 0
    with open('inputs/day3.txt') as f:
        curr_group = []
        for line in f.readlines():
            curr_group.append(line.strip())
            if len(curr_group) == 3:
                common_item = set(curr_group[0]).intersection(set(curr_group[1])).intersection(set(curr_group[2])).pop()
                if common_item.isupper():
                    total += ord(common_item) - ord('A') + 27
                else:
                    total += ord(common_item) - ord('a') + 1

                curr_group.clear()
    print(total)


if __name__ == "__main__":
    # part1()
    part2()