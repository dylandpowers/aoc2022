package main

import (
	"fmt"
	"goaoc22/utils"
)

func Day6() {
	input := utils.GetLines("../inputs/day6.txt")[0]
	window := map[byte]int{}
	for i := 0; i < 13; i++ {
		window[input[i]]++
	}

	for i := 13; i < len(input); i++ {
		window[input[i]]++
		if len(window) == 14 {
			fmt.Println(i + 1)
			return
		}

		thirteenBack := input[i - 13]
		window[thirteenBack]--
		if window[thirteenBack] == 0 {
			delete(window, thirteenBack)
		}
	}
}