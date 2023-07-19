package main

import (
	"fmt"
	"goaoc22/utils"
	"math"
	"strconv"
	"strings"
)

type Directory struct {
	size int
	children map[string]*Directory
}

func (dir *Directory) isDir() bool {
	return dir.size == 0
}

func MakeDir() *Directory {
	return &Directory{
		size: 0,
		children: map[string]*Directory{},
	}
}

func getDirs() *Directory {
	lines := utils.GetLines("../inputs/day7.txt")
	stack := []*Directory{}
	curr := MakeDir()

	for i := 1; i < len(lines); i++ {
		tokens := strings.Split(lines[i], " ")
		if tokens[0] == "$" {
			if tokens[1] == "cd" {
				if tokens[2] == ".." {
					curr = stack[len(stack) - 1]
					stack = stack[:len(stack) - 1]
				} else {
					stack = append(stack, curr)
					if _, ok := curr.children[tokens[2]]; ok {
						curr = curr.children[tokens[2]]
					} else {
						next := MakeDir()
						curr.children[tokens[2]] = next
						curr = next
					}
				}
			}
		} else {
			if tokens[0] == "dir" {
				if _, ok := curr.children[tokens[1]]; !ok {
					curr.children[tokens[1]] = MakeDir()
				}
			} else {
				file := MakeDir()
				size, err := strconv.Atoi(tokens[0])
				if err != nil {
					fmt.Println(err)
					panic(1)
				}
				file.size = size
				curr.children[tokens[1]] = file
			}
		}
	}

	return stack[0]
}

func calculateSize(dir *Directory, sizes *[]int) int {
	size := dir.size
	for _, d := range dir.children {
		size += calculateSize(d, sizes)
	}

	if dir.isDir() {
		*sizes = append(*sizes, size)
	}
	return size
}

func Day7() {
	sizes := []int{}
	totalSize := calculateSize(getDirs(), &sizes)
	unusedSpace := 70_000_000 - totalSize
	spaceToFree := 30_000_000 - unusedSpace

	closest := math.MaxUint32
	for _, size := range sizes {
		if size >= spaceToFree && utils.AbsInt(spaceToFree - size) < utils.AbsInt(spaceToFree - closest) {
			closest = size
		}
	}

	fmt.Println(closest)
}