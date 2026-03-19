function numberOfSubmatrices(grid: string[][]): number {
    const rows = grid.length;
    const cols = grid[0].length;

    const colX = new Array<number>(cols).fill(0);
    const colY = new Array<number>(cols).fill(0);

    let result = 0;

    for (let r = 0; r < rows; r++) {
        let rowX = 0,
            rowY = 0;

        for (let c = 0; c < cols; c++) {
            const cell = grid[r][c];

            if (cell === "X") {
                rowX++;
            } else if (cell === "Y") {
                rowY++;
            }

            colX[c] += rowX;
            colY[c] += rowY;

            if (colX[c] > 0 && colX[c] === colY[c]) {
                result++;
            }
        }
    }

    return result;
}
