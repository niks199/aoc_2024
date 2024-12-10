import operator

class Solution:
    def trailheads(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        ans = 0
        
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '0':
                    self.trailheads = set()
                    self.dfs((row_i, col_i), 0, grid, [])
                    v = len(self.trailheads)
                    ans += v

        return ans

    def dfs(self, pos, expected_el, grid, path):
        n_rows = len(grid)
        n_cols = len(grid[0])

        elev = grid[pos[0]][pos[1]]
        if elev == '.':
            return
        
        if int(elev) != expected_el:
            return
        
        if elev == '9' and expected_el == 9:
            self.trailheads.add(pos)
            return

        moves = [[1, 0], [-1, 0], [0,1], [0,-1]]

        for move in moves:
            n_pos = tuple(map(operator.add, pos, move))

            if 0 <= n_pos[0] < n_rows and 0 <= n_pos[1] < n_cols:
                self.dfs(n_pos, expected_el + 1, grid, path[::] + [pos])

    def trailheads_raiting(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        ans = 0
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '0':
                    ans += self.dfs_part2((row_i, col_i), 0, grid, [])
        return ans

    def dfs_part2(self, pos, expected_el, grid, path):
        n_rows = len(grid)
        n_cols = len(grid[0])

        elev = grid[pos[0]][pos[1]]
        if elev == '.':
            return 0
        
        if int(elev) != expected_el:
            return 0
        
        if elev == '9' and expected_el == 9:
            return 1
        
        moves = [[1, 0], [-1, 0], [0,1], [0,-1]]

        count = 0
        for move in moves:
            n_pos = tuple(map(operator.add, pos, move))

            if 0 <= n_pos[0] < n_rows and 0 <= n_pos[1] < n_cols:
                count += self.dfs_part2(n_pos, expected_el + 1, grid, path[::] + [pos])
        
        return count
