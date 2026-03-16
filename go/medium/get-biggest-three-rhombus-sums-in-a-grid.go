package main

const OFFSET = 50

func getBiggestThree(grid [][]int) []int {
	rows := len(grid)
	cols := len(grid[0])

	diag := make([][]int, 100)
	anti := make([][]int, 100)

	for i := range diag {
		diag[i] = make([]int, cols+1)
		anti[i] = make([]int, rows+1)
	}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			val := grid[r][c]

			diagIdx := r - c + OFFSET
			antiIdx := r + c

			diag[diagIdx][c+1] = diag[diagIdx][c] + val
			anti[antiIdx][r+1] = anti[antiIdx][r] + val
		}
	}

	rhombusSum := func(r, c, d int) int {
		if d == 0 {
			return grid[r][c]
		}

		left, right := c-d, c+d
		top, bottom := r-d, r+d

		diag0 := top - c + OFFSET
		diag1 := r - left + OFFSET

		total := diag[diag0][right+1] - diag[diag0][c]
		total += diag[diag1][c+1] - diag[diag1][left]

		anti0 := top + c
		anti1 := bottom + c

		total += anti[anti0][r] - anti[anti0][top+1]
		total += anti[anti1][bottom] - anti[anti1][r+1]

		return total
	}

	best := []int{-1, -1, -1}
	maxRadius := min(rows, cols) / 2

	for d := 0; d <= maxRadius; d++ {
		for r := d; r < rows-d; r++ {
			for c := d; c < cols-d; c++ {

				val := rhombusSum(r, c, d)

				if val == best[0] || val == best[1] || val == best[2] {
					continue
				}

				if val > best[0] {
					best[2] = best[1]
					best[1] = best[0]
					best[0] = val
				} else if val > best[1] {
					best[2] = best[1]
					best[1] = val
				} else if val > best[2] {
					best[2] = val
				}
			}
		}
	}

	res := []int{}
	for _, v := range best {
		if v != -1 {
			res = append(res, v)
		}
	}
	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}