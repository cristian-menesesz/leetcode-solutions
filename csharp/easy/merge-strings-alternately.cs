string MergeAlternately(string word1, string word2) {
        StringBuilder result = new StringBuilder();
        int minLen = Math.Min(word1.Length, word2.Length);

        for (int i = 0; i < minLen; i++) {
            result.Append(word1[i]);
            result.Append(word2[i]);
        }

        if (word1.Length > minLen) {
            result.Append(word1.Substring(minLen));
        } else if (word2.Length > minLen) {
            result.Append(word2.Substring(minLen));
        }

        return result.ToString();
    }
