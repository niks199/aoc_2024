class Solution:
    def stones(self, inp: str, times):
        stones = [v for v in inp.split(' ')]

        for oo in range(times):
            n = len(stones)

            n_stones = []
            for s_i in range(n):
                parts = self.morph_stone(stones[s_i])
                n_stones.extend(parts)

            stones = n_stones

        return len(stones)
    
    def morph_stone(self, stone):
        if stone == '0':
            return ['1']
        elif len(stone) % 2 == 0:
            v = len(stone)
            return [stone[:v//2], str(int(stone[v//2:]))]
        else:
            return [str(int(stone) * 2024)]

    def stones_part2(self, inp: str, times):
        stones = [v for v in inp.split(' ')]

        freq = {}
        for stone in stones:
            freq.setdefault(stone, 0)
            freq[stone] += 1

        for oo in range(times):
            n_freq = {}
            for stone, count in freq.items():
                parts = self.morph_stone(stone)
                for part in parts:
                    n_freq.setdefault(part, 0)
                    n_freq[part] += 1 * count
            freq = n_freq

        ans = 0
        for k, v in freq.items():
            ans += v

        return ans
