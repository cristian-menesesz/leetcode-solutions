function maxHeightInTime(time: bigint, workerTimes: bigint[]): bigint {
    let totalHeight = 0n;

    for (const workerTime of workerTimes) {
        const limit = (8n * time) / workerTime + 1n;
        const sqrt = bigintSqrt(limit);
        const k = (sqrt - 1n) / 2n;
        totalHeight += k;
    }

    return totalHeight;
}

function minNumberOfSeconds(
    mountainHeight: bigint,
    workerTimes: bigint[],
): bigint {
    if (workerTimes.length === 1) {
        const w = workerTimes[0];
        return (w * mountainHeight * (mountainHeight + 1n)) / 2n;
    }

    let left = 1n;
    let right = (1000000000000n * mountainHeight) / BigInt(workerTimes.length);

    while (left < right) {
        const mid = (left + right) / 2n;

        if (maxHeightInTime(mid, workerTimes) >= mountainHeight) {
            right = mid;
        } else {
            left = mid + 1n;
        }
    }

    return left;
}

// integer sqrt for bigint
function bigintSqrt(n: bigint): bigint {
    if (n < 2n) return n;
    let x0 = n / 2n;
    let x1 = (x0 + n / x0) / 2n;
    while (x1 < x0) {
        x0 = x1;
        x1 = (x0 + n / x0) / 2n;
    }
    return x0;
}
