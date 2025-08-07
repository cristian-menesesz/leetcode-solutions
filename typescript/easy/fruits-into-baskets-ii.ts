function numOfUnplacedFruitsII(fruits: number[], baskets: number[]): number {
    const n = baskets.length;
    let placed = 0;

    for (const fruit of fruits) {
        for (let i = 0; i < n; i++) {
            if (fruit <= baskets[i]) {
                placed++;
                baskets[i] = 0;
                break;
            }
        }
    }

    return n - placed;
}
