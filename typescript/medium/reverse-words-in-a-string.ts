function reverseWords(s: string): string {
    const words = s.split(/\s+/); // split by spaces
    let res: string[] = [];

    for (let i = words.length - 1; i >= 0; i--) {
        res.push(words[i]);
        if (i !== 0) {
            res.push(" ");
        }
    }

    return res.join("");
}
