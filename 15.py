import operator

class Solution:
    def sum_all_boxes(self, inp: str):
        lines = inp.splitlines()

        grid = []
        moves = []
        reading_map = True
        for line in lines:
            if line:
                if reading_map:
                    grid.append(list(line))
                else:
                    moves.extend(list(line))
            else:
                reading_map = False

        n_rows = len(grid)
        n_cols = len(grid[0])

        r_pos = None
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '@':
                    r_pos = (row_i, col_i)
                    break

        m_coord = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

        grid_bounds = [[0, n_rows - 1], [0, n_cols - 1]]

        for (m_i, move) in enumerate(moves):
            scan_r_pos = tuple(map(operator.add, r_pos, m_coord[move]))
            dots = []
            boxes = []
            while all((grid_bounds[i][1] >= scan_r_pos[i] >= grid_bounds[i][0]) for i in [0, 1]):
                if grid[scan_r_pos[0]][scan_r_pos[1]] == '#':
                    break
                elif grid[scan_r_pos[0]][scan_r_pos[1]] == 'O':
                    boxes.append(scan_r_pos)
                elif grid[scan_r_pos[0]][scan_r_pos[1]] == '.':
                    dots.append(scan_r_pos)
                    break
        
                scan_r_pos = tuple(map(operator.add, scan_r_pos, m_coord[move]))

            #print(m_i)
            if len(dots) == 0:
                #self.print_grid(grid)
                continue

            if boxes:
                if len(boxes) > 1:
                    if move in ['>', '<']:
                        min_i = boxes.index(min(boxes, key=lambda x: x[1]))
                        max_i = boxes.index(max(boxes, key=lambda x: x[1]))
                        box_max = tuple(map(operator.add, boxes[max_i], m_coord[move]))
                        box_min = tuple(map(operator.add, boxes[min_i], m_coord[move]))
                        if move == '>':
                            grid[box_max[0]][box_max[1]] = 'O'
                        else:
                            grid[box_min[0]][box_min[1]] = 'O'
                    else:
                        min_i = boxes.index(min(boxes, key=lambda x: x[0]))
                        max_i = boxes.index(max(boxes, key=lambda x: x[0]))
                        box_max = tuple(map(operator.add, boxes[max_i], m_coord[move]))
                        box_min = tuple(map(operator.add, boxes[min_i], m_coord[move]))
                        if move == '^':
                            grid[box_min[0]][box_min[1]] = 'O'
                        else:
                            grid[box_max[0]][box_max[1]] = 'O'
                else:
                    box = boxes[0]
                    box = tuple(map(operator.add, box, m_coord[move]))
                    grid[box[0]][box[1]] = 'O'
            
            grid[r_pos[0]][r_pos[1]] = '.'
            r_pos = tuple(map(operator.add, r_pos, m_coord[move]))
            grid[r_pos[0]][r_pos[1]] = '@'

            #self.print_grid(grid)

        r = self.gps(grid)
        
        return r

    def print_grid(self, grid):
        s = "\n".join([str(g) for g in grid])
        print(s)
        print()
        print()

    def gps(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])

        tot = 0
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == 'O':
                    tot += row_i * 100 + col_i
        return tot

    def sum_all_boxes_expanded(self, inp: str):
        lines = inp.splitlines()

        grid = []
        moves = []
        reading_map = True
        for line in lines:
            if line:
                if reading_map:
                    n_line = []
                    for ch in line:
                        if ch == '#':
                            n_line.extend(['#', '#'])
                        elif ch == 'O':
                            n_line.extend(['[', ']'])
                        elif ch == '.':
                            n_line.extend(['.', '.'])
                        elif ch == '@':
                            n_line.extend(['@', '.'])
                    grid.append(n_line)
                else:
                    moves.extend(list(line))
            else:
                reading_map = False

        n_rows = len(grid)
        n_cols = len(grid[0])

        r_pos = None
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '@':
                    r_pos = (row_i, col_i)
                    break

        self.print_grid(grid)

        m_coord = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

        for (m_i, move) in enumerate(moves):
            #print(f'move: {move}')
            scan_r_pos = tuple(map(operator.add, r_pos, m_coord[move]))

            if grid[scan_r_pos[0]][scan_r_pos[1]] == '.':
                grid[r_pos[0]][r_pos[1]] = '.'
                grid[scan_r_pos[0]][scan_r_pos[1]] = '@'

                #self.print_grid(grid)
                r_pos = scan_r_pos

                continue

            if grid[scan_r_pos[0]][scan_r_pos[1]] == '#':
                #self.print_grid(grid)

                continue

            q = []
            q.append(scan_r_pos)
            boxes = []
            can_move = True
            seen = set()

            while q:
                neigh = q.pop(0)

                if grid[neigh[0]][neigh[1]] == ']':
                    boxes.append(neigh)
                    v = (neigh[0], neigh[1] - 1)
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
                elif grid[neigh[0]][neigh[1]] == '[':
                    boxes.append(neigh)
                    v = (neigh[0], neigh[1] + 1)
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
                
                n_pos = tuple(map(operator.add, neigh, m_coord[move]))

                if grid[n_pos[0]][n_pos[1]] == ']':
                    if n_pos not in seen:
                        seen.add(n_pos)
                        q.append(n_pos)
                elif grid[n_pos[0]][n_pos[1]] == '[':
                    if n_pos not in seen:
                        seen.add(n_pos)
                        q.append(n_pos)
                elif grid[n_pos[0]][n_pos[1]] == '#':
                    can_move = False
                    break


            if not can_move:
                #self.print_grid(grid)
                continue

            if len(boxes) > 0:
                prev_grid = [gr[:] for gr in grid]
                for b in boxes:
                    grid[b[0]][b[1]] = '.'
                new_boxes = [tuple(map(operator.add, box, m_coord[move])) for box in boxes]
                for (i, n_b) in enumerate(new_boxes):
                    old_b = boxes[i]
                    grid[n_b[0]][n_b[1]] = prev_grid[old_b[0]][old_b[1]]

            grid[r_pos[0]][r_pos[1]] = '.'
            grid[scan_r_pos[0]][scan_r_pos[1]] = '@'

            r_pos = scan_r_pos

            #self.print_grid(grid)
            
        r = self.gps_larger(grid)
        
        return r

    def gps_larger(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])

        tot = 0
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == '[':
                    tot += row_i * 100 + col_i
        return tot
