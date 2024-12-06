from collections import deque

class Solution:
    def distinct_positions(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(line)
        
        n_rows = len(grid)
        n_cols = len(grid[0])

        st_pos = None

        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '^':
                    st_pos = (row_i, col_i)
                    break
        
        d = deque()

        d.append((st_pos, 0))

        positions = set()

        positions.add(st_pos)

        moves = {}

        moves[0] = (-1, 0) # U
        moves[1] = (0, 1) # R
        moves[2] = (1, 0) # D
        moves[3] = (0, -1) # L

        while d:
            (pos, dd) = d.popleft()

            positions.add(pos)

            move = moves[dd]

            n_pos = (pos[0] + move[0], pos[1] + move[1])

            if n_pos[0] < 0 or n_pos[0] == n_rows or n_pos[1] < 0 or n_pos[1] == n_cols:
                break

            if grid[n_pos[0]][n_pos[1]] == '#':
                n_dd = (dd + 1) % 4
                move = moves[n_dd]
                n_pos = (pos[0] + move[0], pos[1] + move[1])

                d.append((n_pos, n_dd))
            else:
                d.append((n_pos, dd))

        return len(positions)
    
    def obstruction_positions(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))
        
        n_rows = len(grid)
        n_cols = len(grid[0])

        st_pos = None

        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '^':
                    st_pos = (row_i, col_i)
        
        d = deque()
        d.append((st_pos, 0))
        trail = []
        trail.append((st_pos, 0))
        moves = {}

        moves[0] = (-1, 0) # U
        moves[1] = (0, 1) # R
        moves[2] = (1, 0) # D
        moves[3] = (0, -1) # L

        while d:
            (pos, dd) = d.popleft()

            trail.append((pos, dd))

            move = moves[dd]

            n_pos = (pos[0] + move[0], pos[1] + move[1])

            if n_pos[0] < 0 or n_pos[0] == n_rows or n_pos[1] < 0 or n_pos[1] == n_cols:
                break

            if grid[n_pos[0]][n_pos[1]] == '#':
                n_dd = (dd + 1) % 4
                move = moves[n_dd]
                n_pos = (pos[0] + move[0], pos[1] + move[1])

                d.append((n_pos, n_dd))
            else:
                d.append((n_pos, dd))

        obstructions = set()

        for (pos, dd) in trail:
            v = self.check_circle([row[:] for row in grid], pos, st_pos)
            if v:
                obstructions.add(v)
        return len(obstructions)

    def check_circle(self, grid, st_pos, init_pos):
        d = deque()
        d.append((init_pos, 0))

        moves = {}

        moves[0] = (-1, 0) # U
        moves[1] = (0, 1) # R
        moves[2] = (1, 0) # D
        moves[3] = (0, -1) # L

        n_rows = len(grid)
        n_cols = len(grid[0])

        obst_pos = st_pos

        grid[obst_pos[0]][obst_pos[1]] = '#'

        trail_set = set()

        pos_dd = (init_pos, 0)

        while True:
            if pos_dd in trail_set:
                return obst_pos
            trail_set.add(pos_dd)

            (pos, d) = pos_dd
            move = moves[d]

            n_pos = (pos[0] + move[0], pos[1] + move[1])

            if n_pos[0] < 0 or n_pos[0] == n_rows or n_pos[1] < 0 or n_pos[1] == n_cols:
                return None
            
            if grid[n_pos[0]][n_pos[1]] == '#':
                d = (d + 1) % 4
                pos_dd = (pos, d)
            else:
                pos_dd = (n_pos, d)
