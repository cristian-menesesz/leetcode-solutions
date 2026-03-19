func numberOfSubmatrices(grid [][]byte) int {
	rows := len(grid)
	cols := len(grid[0])

	colX := make([]int, cols)
	colY := make([]int, cols)

	result := 0

	for r := 0; r < rows; r++ {
		rowX, rowY := 0, 0

		for c := 0; c < cols; c++ {
			switch grid[r][c] {
			case 'X':
				rowX++
			case 'Y':
				rowY++
			}

			colX[c] += rowX
			colY[c] += rowY

			if colX[c] > 0 && colX[c] == colY[c] {
				result++
			}
		}
	}

	return result
}