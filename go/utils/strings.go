package utils

import (
	"strconv"
	"strings"
)

func SliceAtoi(slice []string) ([]int, error) {
	conv := make([]int, 0, len(slice))
	for _, str := range slice {
		elem, err := strconv.Atoi(str)
		if err != nil {
			return nil, err
		}
		conv = append(conv, elem)
	}
	return conv, nil
}

func IndexAfter(s string, c string, i int) int {
	newS := s[i:]
	idx := strings.Index(newS, c)
	if idx == -1 {
		return idx
	}
	return idx + i
}