string GcdOfStrings(string str1, string str2) {
    int Gcd(int a, int b) {
        return b == 0 ? a : Gcd(b, a % b);
    }

    int maxLength = Gcd(str1.Length, str2.Length);

    if (str1 + str2 != str2 + str1) {
        return "";
    }

    return str1.Substring(0, maxLength);
}
