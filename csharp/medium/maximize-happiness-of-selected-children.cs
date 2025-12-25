int MaximumHappinessSum(int[] happiness, int k)
{
    Array.Sort(happiness);
    Array.Reverse(happiness); // descending sort

    int happinessSum = 0;
    int decrement = 0;

    for (int i = 0; i < k; i++)
    {
        int currentHappiness = Math.Max(happiness[i] - decrement, 0);
        happinessSum += currentHappiness;
        decrement++;
    }

    return happinessSum;
}