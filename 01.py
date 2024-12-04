class Solution:
    def total_distance(self, left: List[int], right: List[int]):
        heapq.heapify(left)
        heapq.heapify(right)

        total = 0
        while left and right:
            l_v = heapq.heappop(left)
            r_v = heapq.heappop(right)

            d = abs(l_v - r_v)
            total += d

        return total

    def similarity_score(self, left: List[int], right: List[int]):
        freq = {}
        for r in right:
            freq.setdefault(r, 0)
            freq[r] += 1

        for l in left:
            freq.setdefault(l, 0)

        score = 0

        for l in left:
            s = l * freq[l]
            score += l * freq[l]
        
        return score
