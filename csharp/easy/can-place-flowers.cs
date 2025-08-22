bool CanPlaceFlowers(int[] flowerbed, int n)
{
    int plotCounter = 1;
    int flowersPlaced = 0;

    foreach (int plot in flowerbed)
    {
        if (plot == 0)
        {
            plotCounter++;
            if (plotCounter == 3)
            {
                flowersPlaced++;
                plotCounter = 1;
            }
        }
        else
        {
            plotCounter = 0;
        }
    }

    if (plotCounter == 2)
    {
        flowersPlaced++;
    }

    return flowersPlaced >= n;
}
