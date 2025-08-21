function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const maxCandies = Math.max(...candies);
    const ans: boolean[] = [];

    for (let i = 0; i < candies.length; i++) {
        ans.push(candies[i] + extraCandies >= maxCandies);
    }

    return ans;
}
