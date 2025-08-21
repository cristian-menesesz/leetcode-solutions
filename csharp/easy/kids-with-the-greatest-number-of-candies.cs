IList<bool> KidsWithCandies(int[] candies, int extraCandies)
{
    int maxCandies = candies.Max();
    List<bool> ans = new List<bool>();

    for (int i = 0; i < candies.Length; i++)
    {
        ans.Add(candies[i] + extraCandies >= maxCandies);
    }

    return ans;
}
