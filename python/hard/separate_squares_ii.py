import bisect

class SegmentTree:

    def __init__(self, x_coords: list[int]):
        self.x_coords = x_coords
        self.segment_count = len(x_coords) - 1
        self.coverage_count = [0] * (4 * self.segment_count)
        self.covered_length = [0] * (4 * self.segment_count)

    def update(
        self,
        x_left: int,
        x_right: int,
        delta: int,
        left: int,
        right: int,
        node: int,
    ):
        if (
            self.x_coords[right + 1] <= x_left
            or self.x_coords[left] >= x_right
        ):
            return

        if x_left <= self.x_coords[left] and self.x_coords[right + 1] <= x_right:
            self.coverage_count[node] += delta
        else:
            mid = (left + right) // 2
            self.update(x_left, x_right, delta, left, mid, node * 2 + 1)
            self.update(x_left, x_right, delta, mid + 1, right, node * 2 + 2)

        if self.coverage_count[node] > 0:
            self.covered_length[node] = (
                self.x_coords[right + 1] - self.x_coords[left]
            )
        else:
            if left == right:
                self.covered_length[node] = 0
            else:
                self.covered_length[node] = (
                    self.covered_length[node * 2 + 1]
                    + self.covered_length[node * 2 + 2]
                )

    def query_covered_length(self) -> int:
        return self.covered_length[0]

def separateSquares(self, squares: list[list[int]]) -> float:
    sweep_events = []
    x_coord_set = set()

    for x, y, side in squares:
        sweep_events.append((y, 1, x, x + side))
        sweep_events.append((y + side, -1, x, x + side))
        x_coord_set.update([x, x + side])

    x_coords = sorted(x_coord_set)
    segment_tree = self.SegmentTree(x_coords)
    sweep_events.sort()

    area_prefix = []
    active_widths = []

    total_area = 0.0
    previous_y = sweep_events[0][0]

    for y, delta, x_left, x_right in sweep_events:
        covered_width = segment_tree.query_covered_length()
        total_area += covered_width * (y - previous_y)

        segment_tree.update(
            x_left,
            x_right,
            delta,
            0,
            segment_tree.segment_count - 1,
            0,
        )

        area_prefix.append(total_area)
        active_widths.append(segment_tree.query_covered_length())
        previous_y = y

    half_area = (total_area + 1) // 2
    index = bisect.bisect_left(area_prefix, half_area) - 1

    accumulated_area = area_prefix[index]
    width_at_cut = active_widths[index]
    cut_y = sweep_events[index][0]

    return cut_y + (total_area - accumulated_area * 2) / (2.0 * width_at_cut)
