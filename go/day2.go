package main

import (
	"fmt"
	"goaoc22/utils"
)

var scores = map[string]int{
	"AX": 3,
	"AY": 4,
	"AZ": 8,
	"BX": 1,
	"BY": 5,
	"BZ": 9,
	"CX": 2,
	"CY": 6,
	"CZ": 7,
}

func Day2() {
	lines := utils.GetLines("../inputs/day2.txt")

	total := 0
	for _, rawRound := range lines {
		myMove, yourMove := string(rawRound[0]), string(rawRound[2])
		round := myMove + yourMove

		total += scores[round]
	}

	fmt.Println(total)
}