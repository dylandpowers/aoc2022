package utils

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func GetLines(path string) []string {
	elems := []string{}
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		elems = append(elems, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return elems
}

func GetLinesForDay(dayNumber int) []string {
	return GetLines(fmt.Sprintf("../inputs/day%d.txt", dayNumber))
}