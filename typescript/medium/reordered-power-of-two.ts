function reorderedPowerOf2(n: number): boolean {
    function digitFreq(
        x: number
    ): [
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number
    ] {
        const freq: number[] = new Array(10).fill(0);
        while (x > 0) {
            freq[x % 10]++;
            x = Math.floor(x / 10);
        }
        return freq as [
            number,
            number,
            number,
            number,
            number,
            number,
            number,
            number,
            number,
            number
        ];
    }

    if (!("_signatures" in reorderedPowerOf2)) {
        const signatures = new Set<string>();
        for (let i = 0; i < 31; i++) {
            const freq = digitFreq(1 << i);
            signatures.add(JSON.stringify(freq));
        }
        (reorderedPowerOf2 as any)._signatures = signatures;
    }

    const nFreq = digitFreq(n);
    return (reorderedPowerOf2 as any)._signatures.has(JSON.stringify(nFreq));
}
