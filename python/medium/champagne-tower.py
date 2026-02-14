# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

 

# Example 1:

# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
# Example 2:

# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
# Example 3:

# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000
 

# Constraints:

# 0 <= poured <= 109
# 0 <= query_glass <= query_row < 100


class Solution:
    
    MAX_ROWS = 100

    def _cups_until_half(self, row: int) -> int:
        """Number of stored glasses up to middle of row (symmetry compression)."""
        return (row * row + 2 * row + (row % 2)) // 4

    def _overflow(self, x: float) -> float:
        """Amount that spills from a glass."""
        return max(x - 1.0, 0.0)

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0.0

        # symmetry: only compute left half
        col = min(query_glass, query_row - query_glass)

        total_cups = self._cups_until_half(query_row) + col + 1
        cups = [0.0] * total_cups
        cups[0] = float(poured)

        prev_row_start = 0

        # build rows up to query_row - 1
        for r in range(1, query_row):
            row_start = self._cups_until_half(r)

            # left edge
            cups[row_start] = self._overflow(cups[prev_row_start]) / 2

            # middle cells
            for j in range(1, (r + 1) // 2):
                cups[row_start + j] = (
                    self._overflow(cups[prev_row_start + j - 1]) +
                    self._overflow(cups[prev_row_start + j])
                ) / 2

            # center cell (only when even width)
            if r % 2 == 0:
                cups[row_start + r // 2] = self._overflow(
                    cups[prev_row_start + r // 2 - 1]
                )

            prev_row_start = row_start

        # compute only needed part of final row
        final_row_start = self._cups_until_half(query_row)

        if query_row > 0:
            cups[final_row_start] = self._overflow(cups[prev_row_start]) / 2
            for j in range(1, col):
                cups[final_row_start + j] = (
                    self._overflow(cups[prev_row_start + j - 1]) +
                    self._overflow(cups[prev_row_start + j])
                ) / 2

        # return queried glass
        if col == 0:
            return min(1.0, cups[final_row_start])

        if col * 2 == query_row:  # center glass
            return min(1.0, self._overflow(cups[prev_row_start + col - 1]))

        return min(
            1.0,
            (
                self._overflow(cups[prev_row_start + col - 1]) +
                self._overflow(cups[prev_row_start + col])
            ) / 2
        )


# solution works on top of dynamic programming with state compression using symmetry of the champagne pyramid, computing only the necessary half-triangle and propagating overflow row by row

# 1. due to mirror symmetry of the pyramid, any queried glass (r, c) can be mapped to the left half using min(c, r − c), therefore only half of each row needs to be stored and computed
# 2. each glass state depends only on the previous row, where the amount received equals half of the overflow coming from its upper parents
# 3. the dp structure is flattened into a 1-dimensional array, where row offsets are precomputed so each row occupies only the needed half-segment
# 4. edge glasses receive overflow from a single parent, middle glasses receive from two parents, and the center glass (even width row) receives from exactly one symmetric parent
# 5. the final row is not fully computed — only the segment up to the queried column is propagated to avoid unnecessary transitions

# [!] overflow is clamped to positive values only; glasses never store more than capacity 1
# [!] only previous row values are required, therefore full pyramid storage is avoided
# [!] center glasses are treated specially because symmetry collapses two parents into one

# this leads to a progressive simulation of liquid propagation across a compressed triangular dp, evaluating only the necessary states to determine the queried glass


# time complexity: O(r²/2) → O(r²)
# space complexity: O(r²/2) → O(r²) compressed storage for half triangle


# beats 99.76%

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        
        # symmetry: only simulate toward center
        target_col = min(query_glass, query_row - query_glass)

        # amount of liquid reaching each column of current row
        flow = [0.0] * (target_col + 1)
        flow[0] = float(poured)

        # maximum leftward distance liquid can ever reach
        max_left_reach = query_row - target_col + 1

        # first column proven permanently dry
        dry_cutoff = -1

        for row in range(query_row):

            center = row >> 1

            if center >= target_col:
                center, row_is_odd = target_col, 0
            else:
                row_is_odd = row & 1

            # process center glass first (latest to dry)
            overflow = max(flow[center] - 1.0, 0.0)

            if overflow == 0.0:
                return 0.0

            if row_is_odd:
                flow[center + 1] += overflow

            flow[center] = overflow * 0.5

            # propagate outward from center toward edge
            for col in range(center - 1, max(row - max_left_reach, dry_cutoff), -1):
                spill = max(flow[col] - 1.0, 0.0) * 0.5

                if spill == 0.0:
                    dry_cutoff = col
                    break

                flow[col + 1] += spill
                flow[col] = spill

        return min(1.0, flow[target_col])


# solution worked on top of a row-simulation dynamic propagation (DP with state compression) approach, modeling only the reachable liquid flow toward the queried glass using symmetry pruning

# 1. horizontal symmetry of the tower allows mirroring columns, therefore only the nearest side to the center needs to be simulated
# 2. each row depends exclusively on the previous row’s overflow, so a single 1-dimensional state array represents the entire DP layer
# 3. liquid always propagates from center toward borders, meaning the center glass is the last possible position to become dry
# 4. once a column becomes dry, every column further away from the center will also remain dry (monotonic dryness frontier)
# 5. overflow conservation: a glass only transfers (value − 1)/2 to each child, otherwise propagation stops
# 6. reachability bound: liquid cannot travel farther than the geometric limit derived from row distance to the queried glass

# [!] symmetry reduces the simulated state from O(row²) to O(row) without losing correctness
# [!] dryness cutoff enables early termination of propagation within a row
# [!] simulation stops immediately when the center cannot overflow, because no deeper row can receive liquid

# this leads to iteratively propagating overflow from row to row while shrinking the valid computation interval, computing only the physically reachable section of the Pascal-like flow structure


# time complexity: O(n²) worst-case → triangular propagation across rows
# space complexity: O(n) → single compressed DP row storing current liquid flow
