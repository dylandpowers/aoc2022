def part1():
    with open('inputs/day8.txt') as f:
        grid = [[int(d) for d in line.strip()] for line in f.readlines()]

    # number of trees on the outer edges
    visible_trees = set()
    n = len(grid)
    m = len(grid[0])
    # first, the rows
    for i in range(1, n - 1):
        max_height = grid[i][0]

        # L -> R
        for j in range(1, m - 1):
            if grid[i][j] > max_height:
                max_height = grid[i][j]
                visible_trees.add((i, j))

        # R -> L
        max_height = grid[i][m - 1]
        for j in range(m - 2, 0, -1):
            if grid[i][j] > max_height:
                max_height = grid[i][j]
                visible_trees.add((i, j))

    # now, the columns
    for j in range(1, m - 1):
        max_height = grid[0][j]

        # L -> R
        for i in range(1, n - 1):
            if grid[i][j] > max_height:
                max_height = grid[i][j]
                visible_trees.add((i, j))

        # R -> L
        max_height = grid[n - 1][j]
        for i in range(n - 2, 0, -1):
            if grid[i][j] > max_height:
                max_height = grid[i][j]
                visible_trees.add((i, j))

    exterior_trees = n * 2 + m * 2 - 4
    print(len(visible_trees) + exterior_trees)


def part2():
    with open('inputs/day8.txt') as f:
        grid = [[int(d) for d in line.strip()] for line in f.readlines()]

    n = len(grid)
    m = len(grid[0])
    # can always see at least one tree, and we will ignore the edges when calculating the maximum
    viewing_distances = []
    for _ in range(n):
        viewing_distances.append([1] * m)

    # rows first
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            # to the left first
            k = j - 1
            while k >= 0:
                if grid[i][k] >= grid[i][j]:
                    break
                k -= 1
            viewing_distances[i][j] *= j - k if k >= 0 else j

            # to the right
            k = j + 1
            while k < m:
                if grid[i][k] >= grid[i][j]:
                    break
                k += 1
            viewing_distances[i][j] *= k - j if k < m else k - j - 1

    # now columns
    for j in range(1, m - 1):
        for i in range(1, n - 1):
            # up first
            k = i - 1
            while k >= 0:
                if grid[k][j] >= grid[i][j]:
                    break
                k -= 1
            viewing_distances[i][j] *= i - k if k >= 0 else i

            # down
            k = i + 1
            while k < n:
                if grid[k][j] >= grid[i][j]:
                    break
                k += 1
            viewing_distances[i][j] *= k - i if k < n else k - i - 1

    max_scenic_score = max([max(row) for row in viewing_distances])
    print(max_scenic_score)


if __name__ == "__main__":
    part1()
    part2()