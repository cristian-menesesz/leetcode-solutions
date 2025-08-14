function largestGoodInteger(num: string): string {
    let count = 1;
    let ans = -1;

    for (let i = 1; i < num.length; i++) {
        if (num[i] === num[i - 1]) {
            count++;
            if (count === 3) {
                ans = Math.max(ans, parseInt(num[i]));
            }
        } else {
            count = 1;
        }
    }

    return ans !== -1 ? String(ans).repeat(3) : "";
}
