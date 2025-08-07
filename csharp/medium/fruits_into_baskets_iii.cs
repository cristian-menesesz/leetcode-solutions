int NumOfUnplacedFruitsSegmentTree(int[] fruits, int[] baskets)
{
    int n = baskets.Length;
    int ans = 0;
    int power = 1;

    while (power < n)
    {
        power *= 2;
    }

    int[] segmentTree = new int[power * 2];

    for (int i = 0; i < n; i++)
    {
        segmentTree[power + i] = baskets[i];
    }

    for (int i = power - 1; i > 0; i--)
    {
        segmentTree[i] = Math.Max(segmentTree[2 * i], segmentTree[2 * i + 1]);
    }

    foreach (int fruit in fruits)
    {
        if (segmentTree[1] < fruit)
        {
            ans++;
            continue;
        }

        int i = 1;
        while (i < power)
        {
            i *= 2;
            if (segmentTree[i] < fruit)
            {
                i += 1;
            }
        }

        segmentTree[i] = 0;

        i /= 2;
        while (i > 0)
        {
            segmentTree[i] = Math.Max(segmentTree[2 * i], segmentTree[2 * i + 1]);
            i /= 2;
        }
    }

    return ans;
}
