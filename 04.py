class Solution:
    def xmas(self, grid: str):
        lines = [l for l in grid.split('\n') if l]

        n_cols = len(lines[0])
        n_rows = len(lines)

        tot = 0
        tot_rays = []
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if lines[row_i][col_i] == 'X':
                    pos = (row_i, col_i)
                    rays = self.find_at_lines(lines, pos)
                    tot_rays.extend(rays)
                    v = len(rays)
                    tot += v
        return tot

    def find_at_lines(self, lines, pos):
        n_cols = len(lines[0])
        n_rows = len(lines)

        mm = [[], [], [], [], [], [], [], []]
        letters = 'XMAS'

        for i in range(0, 4):
            mm[0].append((letters[i], (pos[0], pos[1] + i)))
            mm[1].append((letters[i], (pos[0], pos[1] - i)))

            mm[2].append((letters[i], (pos[0] + i, pos[1])))
            mm[3].append((letters[i], (pos[0] - i, pos[1])))

            mm[4].append((letters[i], (pos[0] - i, pos[1] - i)))
            mm[5].append((letters[i], (pos[0] - i, pos[1] + i)))

            mm[6].append((letters[i], (pos[0] + i, pos[1] - i)))
            mm[7].append((letters[i], (pos[0] + i, pos[1] + i)))

        rays = []

        for ray in mm:
            done = True
            for (letter, pos) in ray:
                if pos[0] < 0 or pos[0] >= n_rows or pos[1] < 0 or pos[1] >= n_cols:
                    done = False
                    break
                if lines[pos[0]][pos[1]] != letter:
                    done = False
                    break
            if done:
                rays.append(ray[::])

        return rays

    def x_mas(self, grid: str):
        lines = [l for l in grid.split('\n') if l]

        n_cols = len(lines[0])
        n_rows = len(lines)

        tot = 0
        tot_rays = []
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if lines[row_i][col_i] == 'A':
                    pos = (row_i, col_i)
                    v = self.find_cross(lines, pos)
                    tot += v
        
        return tot

    def find_cross(self, lines: str, pos):
        mm = [[], [], [], []]

        # M S
        #  A
        # M S

        mm[0].append(((pos[0] - 1, pos[1] - 1), 'M')) # top-left
        mm[0].append(((pos[0] - 1, pos[1] + 1), 'S')) # top-right
        mm[0].append((pos, 'A'))
        mm[0].append(((pos[0] + 1, pos[1] - 1), 'M')) # bottom left
        mm[0].append(((pos[0] + 1, pos[1] + 1), 'S')) # bottom right

        # M M
        #  A
        # S S
        mm[1].append(((pos[0] - 1, pos[1] - 1), 'M'))# top-left
        mm[1].append(((pos[0] - 1, pos[1] + 1), 'M'))# top-right
        mm[1].append((pos, 'A'))
        mm[1].append(((pos[0] + 1, pos[1] - 1), 'S'))# bottom left
        mm[1].append(((pos[0] + 1, pos[1] + 1), 'S'))# bottom right

        # S M
        #  A
        # S M
        mm[2].append(((pos[0] - 1, pos[1] - 1), 'S'))# top-left
        mm[2].append(((pos[0] - 1, pos[1] + 1), 'M'))# top-right
        mm[2].append((pos, 'A'))
        mm[2].append(((pos[0] + 1, pos[1] - 1), 'S'))# bottom left
        mm[2].append(((pos[0] + 1, pos[1] + 1), 'M'))# bottom right

        # S S
        #  A
        # M M
        mm[3].append(((pos[0] - 1, pos[1] - 1), 'S'))# top-left
        mm[3].append(((pos[0] - 1, pos[1] + 1), 'S'))# top-right
        mm[3].append((pos, 'A'))
        mm[3].append(((pos[0] + 1, pos[1] - 1), 'M'))# bottom left
        mm[3].append(((pos[0] + 1, pos[1] + 1), 'M'))# bottom right

        n_cols = len(lines[0])
        n_rows = len(lines)

        count = 0
        for m in mm:
            done = True
            for (pos, letter) in m:
                if pos[0] < 0 or pos[0] >= n_rows or pos[1] < 0 or pos[1] >= n_cols:
                    done = False
                    break
                if letter != lines[pos[0]][pos[1]]:
                    done = False
                    break
            if done:
                count += 1

        return count
