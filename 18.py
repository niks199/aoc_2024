import re
from collections import deque
import operator
class Solution:
    def steps_needed(self, inp: str, n_rows: int, n_cols: int, byte_count: int):
        lines = inp.splitlines()

        pattern = "([0-9]+),([0-9]+)"

        bytes = []

        for line in lines:
            result = re.findall(pattern, line)
            v = [int(r) for r in result[0]]
            bytes.append(v)
  

        grid = [['.'] * n_cols for _ in range(n_rows)]

        for b_i in range(byte_count):
            byte = bytes[b_i]
            grid[byte[1]][byte[0]] = '#'


        grid_bounds = [[0, n_rows - 1], [0, n_cols - 1]]

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        d = deque()

        d.append(((0, 0), 0))

        seen = set()
        seen.add((0,0))

        while d:
            (pos, dist) = d.popleft()

            if pos == (n_rows - 1, n_cols - 1):
                return dist
            
            for m in moves:
                n_pos = tuple(map(operator.add, pos, m))

                if all((grid_bounds[i_b][1] >= n_pos[i_b] >= grid_bounds[i_b][0]) for i_b in [0, 1]) and \
                    n_pos not in seen and grid[n_pos[0]][n_pos[1]] != '#':
                    d.append((n_pos, dist + 1))
                    seen.add(n_pos)

        return -1
    
    def cut_off(self, inp: str, n_rows: int, n_cols: int, byte_count: int):
        lines = inp.splitlines()

        pattern = "([0-9]+),([0-9]+)"

        bytes = []

        for line in lines:
            result = re.findall(pattern, line)
            v = [int(r) for r in result[0]]
            bytes.append(v)
  

        grid = [['.'] * n_cols for _ in range(n_rows)]

        last_b_i = 0
        for b_i in range(byte_count):
            byte = bytes[b_i]
            grid[byte[1]][byte[0]] = '#'
            last_b_i = b_i

        n_bytes = len(bytes)
        ans = None
        for b_i in range(last_b_i, n_bytes):
            byte = bytes[b_i]
            grid[byte[1]][byte[0]] = '#'
            print(byte)

            ans = byte
            res = self.simulate(grid)
            if res == -1:
                break
        
        return ans

    def simulate(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])

        grid_bounds = [[0, n_rows - 1], [0, n_cols - 1]]

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        d = deque()

        d.append(((0, 0), 0))

        seen = set()
        seen.add((0,0))

        while d:
            (pos, dist) = d.popleft()

            if pos == (n_rows - 1, n_cols - 1):
                return dist
            
            for m in moves:
                n_pos = tuple(map(operator.add, pos, m))

                if all((grid_bounds[i_b][1] >= n_pos[i_b] >= grid_bounds[i_b][0]) for i_b in [0, 1]) and \
                    n_pos not in seen and grid[n_pos[0]][n_pos[1]] != '#':
                    d.append((n_pos, dist + 1))
                    seen.add(n_pos)

        return -1
