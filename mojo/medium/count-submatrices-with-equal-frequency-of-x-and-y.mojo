fn numberOfSubmatrices(grid: List[List[String]]) -> Int:
    let rows = len(grid)
    let cols = len(grid[0])

    var col_x = [0] * cols
    var col_y = [0] * cols

    var result: Int = 0

    for r in range(rows):
        var row_x: Int = 0
        var row_y: Int = 0

        for c in range(cols):
            let cell = grid[r][c]

            if cell == "X":
                row_x += 1
            elif cell == "Y":
                row_y += 1

            col_x[c] += row_x
            col_y[c] += row_y

            if col_x[c] > 0 and col_x[c] == col_y[c]:
                result += 1

    return result