package main

import "math"

func maxHeightInTime(time int64, workerTimes []int64) int64 {
	var totalHeight int64 = 0

	for _, workerTime := range workerTimes {
		limit := (8*time)/workerTime + 1
		k := (int64(math.Sqrt(float64(limit))) - 1) / 2
		totalHeight += k
	}

	return totalHeight
}

func minNumberOfSeconds(mountainHeight int64, workerTimes []int64) int64 {

	if len(workerTimes) == 1 {
		w := workerTimes[0]
		return w * mountainHeight * (mountainHeight + 1) / 2
	}

	left := int64(1)
	right := (1_000_000_000_000 * mountainHeight) / int64(len(workerTimes))

	for left < right {
		mid := (left + right) / 2

		if maxHeightInTime(mid, workerTimes) >= mountainHeight {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}