package main

import (
	"fmt"
	"goaoc22/utils"
	"strconv"
	"strings"
)

func Day5() {
	lines := utils.GetLines("../inputs/Day5.txt")

	finishedReadingStacks := false
	stacks := [9][]string{}
	// for idx := range stacks {
	// 	stacks[idx] = []string{}
	// }

	for _, line := range lines {
		if line == "" {
			continue
		}

		if line[1] == '1' {
			// this is the numbering line
			finishedReadingStacks = true
			continue
		}

		if !finishedReadingStacks {
			for i := 0; i < len(line); i += 4 {
				if line[i] == ' ' {
					// no crate here
					continue
				}

				stacks[i / 4] = append([]string{string(line[i + 1])}, stacks[i / 4]...)
			}
		} else {
			numToMove, err := strconv.Atoi(line[5:utils.IndexAfter(line, " ", 5)])
			if err != nil {
				fmt.Println(err)
				return
			}

			fromStackIdx := int(line[strings.Index(line, "from") + 5] - '0') - 1
			toStackIdx := int(line[strings.Index(line, "from") + 10] - '0') - 1

			for i := 0; i < numToMove; i++ {
				top := stacks[fromStackIdx][len(stacks[fromStackIdx]) - 1]
				stacks[fromStackIdx] = stacks[fromStackIdx][:len(stacks[fromStackIdx]) - 1]
				// fmt.Println("To before: ", stacks[toStackIdx])
				stacks[toStackIdx] = append(stacks[toStackIdx], top)
			}
		}
	}

	var sb strings.Builder
	for _, stack := range stacks {
		sb.WriteString(stack[len(stack) - 1])
	}

	fmt.Println(sb.String())
}