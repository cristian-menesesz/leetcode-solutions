function numOfUnplacedFruitsIII(fruits: number[], baskets: number[]): number {
    const n = baskets.length;
    let ans = 0;

    let power = 1;
    while (power < n) {
        power *= 2;
    }

    const segmentedTree: number[] = new Array(power * 2).fill(0);

    for (let i = 0; i < n; i++) {
        segmentedTree[power + i] = baskets[i];
    }

    for (let i = power - 1; i > 0; i--) {
        segmentedTree[i] = Math.max(
            segmentedTree[2 * i],
            segmentedTree[2 * i + 1]
        );
    }

    for (const fruit of fruits) {
        if (segmentedTree[1] < fruit) {
            ans++;
            continue;
        }

        let i = 1;
        while (i < power) {
            i *= 2;
            if (segmentedTree[i] < fruit) {
                i++;
            }
        }

        segmentedTree[i] = 0;
        i = Math.floor(i / 2);
        while (i > 0) {
            segmentedTree[i] = Math.max(
                segmentedTree[2 * i],
                segmentedTree[2 * i + 1]
            );
            i = Math.floor(i / 2);
        }
    }

    return ans;
}
