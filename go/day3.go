package main

import (
	"fmt"
	"goaoc22/utils"
)

func Day3() {
	lines := utils.GetLines("../inputs/day3.txt")

	priorities := 0
	for i := 0; i < len(lines); i += 3 {
		elf1, elf2, elf3 := lines[i], lines[i + 1], lines[i + 2]
		seen := map[byte]bool{}
		for j := 0; j < len(elf1); j++ {
			seen[elf1[j]] = true
		}

		intersection := map[byte]bool{}
		for j := 0; j < len(elf2); j++ {
			if _, ok := seen[elf2[j]]; ok {
				intersection[elf2[j]] = true
			}
		}

		for j := 0; j < len(elf3); j++ {
			curr := elf3[j]
			if _, ok := intersection[curr]; ok {
				if 'A' <= curr && curr <= 'Z' {
					priorities += int(curr - 'A' + 27)
				} else {
					priorities += int(curr - 'a' + 1)
				}
				break
			}
		}
	}

	fmt.Println(priorities)
}