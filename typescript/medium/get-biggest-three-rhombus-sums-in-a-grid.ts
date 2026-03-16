const OFFSET = 50;

function getBiggestThree(grid: number[][]): number[] {
    const rows = grid.length;
    const cols = grid[0].length;

    const diag = Array.from({ length: 100 }, () => new Array(cols + 1).fill(0));
    const anti = Array.from({ length: 100 }, () => new Array(rows + 1).fill(0));

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const val = grid[r][c];

            const diagIdx = r - c + OFFSET;
            const antiIdx = r + c;

            diag[diagIdx][c + 1] = diag[diagIdx][c] + val;
            anti[antiIdx][r + 1] = anti[antiIdx][r] + val;
        }
    }

    function rhombusSum(r: number, c: number, d: number): number {
        if (d === 0) return grid[r][c];

        const left = c - d,
            right = c + d;
        const top = r - d,
            bottom = r + d;

        const diag0 = top - c + OFFSET;
        const diag1 = r - left + OFFSET;

        let total =
            diag[diag0][right + 1] -
            diag[diag0][c] +
            diag[diag1][c + 1] -
            diag[diag1][left];

        const anti0 = top + c;
        const anti1 = bottom + c;

        total += anti[anti0][r] - anti[anti0][top + 1];
        total += anti[anti1][bottom] - anti[anti1][r + 1];

        return total;
    }

    const best = [-1, -1, -1];
    const maxRadius = Math.floor(Math.min(rows, cols) / 2);

    for (let d = 0; d <= maxRadius; d++) {
        for (let r = d; r < rows - d; r++) {
            for (let c = d; c < cols - d; c++) {
                const val = rhombusSum(r, c, d);

                if (best.includes(val)) continue;

                if (val > best[0]) {
                    best[2] = best[1];
                    best[1] = best[0];
                    best[0] = val;
                } else if (val > best[1]) {
                    best[2] = best[1];
                    best[1] = val;
                } else if (val > best[2]) {
                    best[2] = val;
                }
            }
        }
    }

    return best.filter((x) => x !== -1);
}
