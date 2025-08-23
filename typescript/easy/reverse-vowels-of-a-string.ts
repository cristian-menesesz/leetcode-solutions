function reverseVowels(s: string): string {
    let chars = s.split("");
    let n = chars.length;
    const vowels = new Set("aeiouAEIOU");

    for (let i = 0; i < n; i++) {
        console.log(n);
        if (vowels.has(chars[i])) {
            for (let j = n - 1; j > i; j--) {
                n -= 1;
                if (vowels.has(chars[j])) {
                    [chars[i], chars[j]] = [chars[j], chars[i]];
                    break;
                }
            }
        }
    }

    return chars.join("");
}
