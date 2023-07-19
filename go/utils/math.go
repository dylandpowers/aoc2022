package utils

func MaxInts(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func AbsInt(a int) int {
	if a < 0 {
		return -a
	}
	return a
}