from collections import deque
import operator
class Solution:
    def price_of_fencing(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))

        seen = set()

        n_rows = len(grid)
        n_cols = len(grid[0])

        ans = 0
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                pos = (row_i, col_i)
                if pos not in seen:
                    p = self.price_for_region(pos, grid, seen)
                    ans += p
        
        return ans

    def price_for_region(self, pos, grid, seen):
        d = deque()

        plant = grid[pos[0]][pos[1]]

        d.append((pos, plant))
        seen.add(pos)

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        n_rows = len(grid)
        n_cols = len(grid[0])

        perim = 0
        area = 0

        while d:
            (pos, p) = d.popleft()

            area += 1

            for m in moves:
                n_pos = tuple(map(operator.add, pos, m))

                if n_rows > n_pos[0] >= 0 and n_cols > n_pos[1] >= 0:
                    if grid[n_pos[0]][n_pos[1]] != p:
                        perim += 1
                else:
                    perim += 1
                
            for m in moves:
                n_pos = tuple(map(operator.add, pos, m))
                if n_rows > n_pos[0] >= 0 and n_cols > n_pos[1] >= 0 and grid[n_pos[0]][n_pos[1]] == p and n_pos not in seen:
                    seen.add(n_pos)
                    d.append((n_pos, p))
        
        return area * perim

    def price_of_fencing_part2(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        n_rows_2 = len(grid) + 2
        n_cols_2 = len(grid[0]) + 2

        grid2 = [['1'] * n_cols_2 for _ in range(n_rows_2)]

        for pos in [(0, 0), (n_rows_2 - 1, n_cols_2 - 1), (n_rows_2 - 1, 0), (0, n_cols_2 - 1)]:
            grid2[pos[0]][pos[1]] = '2'


        for row_i in range(n_rows):
            for col_i in range(n_cols):
                pos_2 = (row_i + 1, col_i + 1)
                grid2[pos_2[0]][pos_2[1]] = grid[row_i][col_i]

        seen = set()

        ans = 0
        for row_i in range(n_rows_2):
            for col_i in range(n_cols_2):
                pos = (row_i, col_i)
                if pos not in seen:
                    if grid2[pos[0]][pos[1]] not in ['1', '2']:
                        if grid2[pos[0]][pos[1]] == 'C':
                            pass
                        p = self.price_for_region_part2(pos, grid2, seen)
                        ans += p
        
        return ans

    def price_for_region_part2(self, pos, grid, seen):
        d = deque()

        plant = grid[pos[0]][pos[1]]

        d.append((pos, plant))
        seen.add(pos)

        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        n_rows = len(grid)
        n_cols = len(grid[0])

        area = 0

        seen_outer_block = set()
        side_counter = 0

        while d:
            (pos, p) = d.popleft()

            area += 1


            for (m_i, m) in enumerate(moves):
                n_pos = tuple(map(operator.add, pos, m))

                if n_rows > n_pos[0] >= 0 and n_cols > n_pos[1] >= 0:
                    outer_p = grid[n_pos[0]][n_pos[1]]
                    outer = (n_pos, m_i)

                    if outer_p != p and outer not in seen_outer_block:
                        r = self.move_along_side(outer, (pos, p), grid, seen_outer_block)
                        if r:
                            side_counter += 1
            
            for m in moves:
                n_pos = tuple(map(operator.add, pos, m))
                if n_rows > n_pos[0] >= 0 and n_cols > n_pos[1] >= 0 and grid[n_pos[0]][n_pos[1]] == p and n_pos not in seen:
                    seen.add(n_pos)
                    d.append((n_pos, p))

        v = area * side_counter

        #print(f'{plant} {area} {side_counter}')
        return v

    def move_along_side(self, outer, inner, grid, seen_side):
        d = deque()

        m_i = outer[1]

        if (inner[0], m_i) in seen_side:
            return False
        
        seen_side.add((inner[0], m_i))

        moves = []
        if outer[1] in [0, 1]:
            moves = [(0, 1), (0, -1)]
        elif outer[1] in [2, 3]:
            moves = [(1, 0), (-1, 0)]

        all_moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        d.append(inner[0])

        n_rows = len(grid)
        n_cols = len(grid[0])

        while d:
            (inner_cur) = d.popleft()

            for m in moves:
                n_pos = tuple(map(operator.add, inner_cur, m))
                n_outer_pos = tuple(map(operator.add, n_pos, all_moves[m_i]))

                if n_rows > n_pos[0] >= 0 and n_cols > n_pos[1] >= 0 and \
                    grid[n_pos[0]][n_pos[1]] == inner[1] and \
                        grid[n_outer_pos[0]][n_outer_pos[1]] != inner[1] and \
                            (n_pos, m_i) not in seen_side:
                    seen_side.add((n_pos, m_i))
                    d.append(n_pos)

        return True
