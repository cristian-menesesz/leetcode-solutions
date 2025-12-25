function maximumHappinessSum(happiness: number[], k: number): number {
    happiness.sort((a, b) => b - a); // descending sort

    let happinessSum = 0;
    let decrement = 0;

    for (let i = 0; i < k; i++) {
        const currentHappiness = Math.max(happiness[i] - decrement, 0);
        happinessSum += currentHappiness;
        decrement++;
    }

    return happinessSum;
}
