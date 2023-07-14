package main

import (
	"fmt"
	"goaoc22/utils"
	"strings"
)

func Day4() {
	lines := utils.GetLines("../inputs/day4.txt")

	numOverlapping := 0
	for _, line := range lines {
		assignments := strings.Split(line, ",")
		first, err1 := utils.SliceAtoi(strings.Split(assignments[0], "-"))
		second, err2 := utils.SliceAtoi(strings.Split(assignments[1], "-"))

		if err1 != nil || err2 != nil {
			fmt.Println(err1, err2)
			return
		}

		if first[0] <= second[0] && first[1] >= second[0] {
			numOverlapping++
		} else if second[0] <= first[0] && second[1] >= first[0] {
			numOverlapping++
		}
	}

	fmt.Println(numOverlapping)
}