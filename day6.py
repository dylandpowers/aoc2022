from collections import defaultdict


def part1():
    with open('inputs/day6.txt') as f:
        stream = f.readline().strip()

    window = defaultdict(int)
    for i in range(len(stream)):
        c = stream[i]
        window[c] += 1
        if len(window) == 4:
            print(i + 1)
            return

        if i >= 3:
            three_back = stream[i - 3]
            window[three_back] -= 1
            if window[three_back] == 0:
                del window[three_back]



def part2():
    with open('inputs/day6.txt') as f:
        stream = f.readline().strip()

    window = defaultdict(int)
    for i in range(len(stream)):
        c = stream[i]
        window[c] += 1
        if len(window) == 14:
            print(i + 1)
            return

        if i >= 13:
            thirteen_back = stream[i - 13]
            window[thirteen_back] -= 1
            if window[thirteen_back] == 0:
                del window[thirteen_back]


if __name__ == '__main__':
    part1()
    part2()
