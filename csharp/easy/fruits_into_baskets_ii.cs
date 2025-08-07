int NumOfUnplacedFruits(int[] fruits, int[] baskets)
{
    int n = baskets.Length;
    int placed = 0;

    foreach (int fruit in fruits)
    {
        for (int i = 0; i < n; i++)
        {
            if (fruit <= baskets[i])
            {
                placed++;
                baskets[i] = 0;
                break;
            }
        }
    }

    return n - placed;
}
