string ReverseWords(string s)
{
    string[] words = s.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
    List<string> res = new List<string>();

    for (int i = words.Length - 1; i >= 0; i--)
    {
        res.Add(words[i]);
        if (i != 0)
        {
            res.Add(" ");
        }
    }

    return string.Join("", res);
}
