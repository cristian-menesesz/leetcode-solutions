import (
	"container/heap"
	"sort"
)

type Room struct {
	time int
	id   int
}

type MinHeap []Room
func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	if h[i].time == h[j].time {
		return h[i].id < h[j].id
	}
	return h[i].time < h[j].time
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(Room)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func mostBooked(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})

	free := &MinHeap{}
	busy := &MinHeap{}
	heap.Init(free)
	heap.Init(busy)

	for i := 0; i < n; i++ {
		heap.Push(free, Room{0, i})
	}

	count := make([]int, n)

	for _, m := range meetings {
		start, end := m[0], m[1]
		dur := end - start

		for busy.Len() > 0 && (*busy)[0].time <= start {
			r := heap.Pop(busy).(Room)
			heap.Push(free, Room{0, r.id})
		}

		var room int
		if free.Len() > 0 {
			r := heap.Pop(free).(Room)
			room = r.id
			heap.Push(busy, Room{end, room})
		} else {
			r := heap.Pop(busy).(Room)
			room = r.id
			heap.Push(busy, Room{r.time + dur, room})
		}
		count[room]++
	}

	maxIdx := 0
	for i := range count {
		if count[i] > count[maxIdx] {
			maxIdx = i
		}
	}
	return maxIdx
}
