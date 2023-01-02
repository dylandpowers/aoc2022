from array import array


class Dir:
    def __init__(self) -> None:
        self.children: dict = {}
        self.size: int = 0

    def is_dir(self) -> bool:
        return self.size == 0

    def __str__(self) -> str:
        return self.children.__str__() + " " + str(self.size)


def get_dirs():
    with open('inputs/day7.txt') as f:
        f.readline() # first line is irrelevant
        stack = []
        curr = Dir()
        for line in f.readlines():
            tokens = line.strip().split()
            if tokens[0] == '$':
                if tokens[1] == 'cd':
                    if tokens[2] == '..':
                        curr = stack.pop()
                    else:
                        stack.append(curr)
                        if tokens[2] in curr.children:
                            curr = curr.children[tokens[2]]
                        else:
                            next = Dir()
                            curr.children[tokens[2]] = next
                            curr = next
                else:
                    # this is an ls, do nothing
                    pass
            else:
                # we are currently in an ls
                if tokens[0] == 'dir':
                    if tokens[1] not in curr.children:
                        curr.children[tokens[1]] = Dir()
                else:
                    dir_file = Dir()
                    dir_file.size = int(tokens[0])
                    curr.children[tokens[1]] = dir_file
        return stack[0] if len(stack) > 0 else curr



def part1():
    top = get_dirs()

    def calculate_size(dir: Dir, sizes: array) -> int:
        size = dir.size
        for d in dir.children.values():
            size += calculate_size(d, sizes)

        if dir.is_dir() and size < 100_000:
            sizes.append(size)
        return size

    sizes = []
    calculate_size(top, sizes)
    print(sum(sizes))



def part2():
    top = get_dirs()

    def calculate_size(dir: Dir, sizes: array) -> int:
        size = dir.size
        for d in dir.children.values():
            size += calculate_size(d, sizes)

        if dir.is_dir():
            sizes.append(size)
        return size

    sizes = []
    total_size = calculate_size(top, sizes)

    unused_space = 70_000_000 - total_size
    space_to_free = 30_000_000 - unused_space

    closest = float('inf')
    for size in sizes:
        if size >= space_to_free and abs(space_to_free - size) < abs(space_to_free - closest):
            closest = size

    print(closest)


if __name__ == "__main__":
    part1()
    part2()