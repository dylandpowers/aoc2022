package main

import (
	"fmt"
	"goaoc22/utils"
	"sort"
	"strconv"
)

func Day1() {
	lines := utils.GetLines("../inputs/day1.txt")
	calsPerElf := []int{}

	total, max := 0, 0
	for _, cals := range lines {
		if cals == "" {
			max = utils.Max(max, total)
			calsPerElf = append(calsPerElf, total)
			total = 0
			continue
		}

		calsInt, _ := strconv.Atoi(cals)
		total += calsInt
	}

	calsPerElf = append(calsPerElf, total)
	sort.Ints(calsPerElf)

	total = 0
	for _, cals := range calsPerElf[len(calsPerElf) - 3:] {
		total += cals
	}
	fmt.Println(total)
}