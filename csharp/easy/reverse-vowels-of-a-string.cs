string ReverseVowels(string s)
{
    char[] chars = s.ToCharArray();
    int n = chars.Length;
    HashSet<char> vowels = new HashSet<char>("aeiouAEIOU".ToCharArray());

    for (int i = 0; i < n; i++)
    {
        Console.WriteLine(n);
        if (vowels.Contains(chars[i]))
        {
            for (int j = n - 1; j > i; j--)
            {
                n--;
                if (vowels.Contains(chars[j]))
                {
                    char temp = chars[i];
                    chars[i] = chars[j];
                    chars[j] = temp;
                    break;
                }
            }
        }
    }

    return new string(chars);
}
