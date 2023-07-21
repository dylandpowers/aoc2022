package main

import (
	"fmt"
	"goaoc22/utils"
)

type coordinate struct {
	x int
	y int
}

func Day8() {
	lines := utils.GetLinesForDay(8)
	visibleTrees := map[coordinate]bool{}
	m, n := len(lines), len(lines[0])

	// rows
	for i := 1; i < m - 1; i++ {
		maxHeight := lines[i][0]

		// left -> right
		for j := 1; j < n - 1; j++ {
			if lines[i][j] > maxHeight {
				visibleTrees[coordinate{i, j}] = true
				maxHeight = lines[i][j]
			}
		}

		// right -> left
		maxHeight = lines[i][n - 1]
		for j := n - 2; j > 0; j-- {
			if lines[i][j] > maxHeight {
				visibleTrees[coordinate{i, j}] = true
				maxHeight = lines[i][j]
			}
		}
	}

	// columns
	for j := 1; j < n - 1; j++ {
		maxHeight := lines[0][j]

		// top -> bottom
		for i := 1; i < m - 1; i++ {
			if lines[i][j] > maxHeight {
				visibleTrees[coordinate{i, j}] = true
				maxHeight = lines[i][j]
			}
		}

		// bottom -> top
		maxHeight = lines[m - 1][j]
		for i := m - 2; i > 0; i-- {
			if lines[i][j] > maxHeight {
				visibleTrees[coordinate{i, j}] = true
				maxHeight = lines[i][j]
			}
		}
	}

	outsideTrees := n * 2 + m * 2 - 4
	fmt.Println(len(visibleTrees) + outsideTrees)
}