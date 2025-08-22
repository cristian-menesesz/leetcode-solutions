function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let plotCounter = 1;
    let flowersPlaced = 0;

    for (let plot of flowerbed) {
        if (plot === 0) {
            plotCounter++;
            if (plotCounter === 3) {
                flowersPlaced++;
                plotCounter = 1;
            }
        } else {
            plotCounter = 0;
        }
    }

    if (plotCounter === 2) {
        flowersPlaced++;
    }

    return flowersPlaced >= n;
}
