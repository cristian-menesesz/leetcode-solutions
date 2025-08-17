function mergeAlternately(word1: string, word2: string): string {
    let result: string[] = [];
    const minLen = Math.min(word1.length, word2.length);

    for (let i = 0; i < minLen; i++) {
        result.push(word1[i]);
        result.push(word2[i]);
    }

    if (word1.length > minLen) {
        result.push(word1.slice(minLen));
    } else if (word2.length > minLen) {
        result.push(word2.slice(minLen));
    }

    return result.join("");
}
