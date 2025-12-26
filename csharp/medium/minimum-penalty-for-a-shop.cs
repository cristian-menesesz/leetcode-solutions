int BestClosingTime(string customers)
{
    int penalty = 0;

    foreach (char c in customers)
    {
        if (c == 'Y') penalty++;
    }

    int minPenalty = penalty;
    int bestHour = 0;

    for (int i = 0; i < customers.Length; i++)
    {
        char c = customers[i];

        if (c == 'Y')
        {
            penalty -= 1;
        }
        else
        {
            penalty += 1;
        }

        if (penalty < minPenalty)
        {
            minPenalty = penalty;
            bestHour = i + 1;
        }
    }

    return bestHour;
}
