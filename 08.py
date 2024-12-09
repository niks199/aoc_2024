import math
import operator
class Solution:
    def unique_locations(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        antennas = {}
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] != '.':
                    antennas.setdefault(grid[row_i][col_i], [])
                    antennas[grid[row_i][col_i]].append((row_i, col_i))

        antinodes = set()

        for k, antenna_block in antennas.items():
            n_b = len(antenna_block)

            if n_b < 2:
                continue

            for i in range(n_b):
                for j in range(i + 1, n_b):
                    for pair in [(antenna_block[i], antenna_block[j]), (antenna_block[j], antenna_block[i])]:
                        v = tuple(map(operator.sub, pair[1], pair[0]))
                        v_m = math.sqrt(v[0] * v[0] + v[1] * v[1])
                        u = tuple(map(operator.truediv, v, (v_m, v_m)))

                        d = 2 * v_m

                        d_u = tuple(map(operator.mul, (d, d), u))
                        d_u = (int(d_u[0]), int(d_u[1]))
                        coord = tuple(map(operator.add, d_u, pair[0]))

                        if n_rows > coord[0] >= 0 and n_cols > coord[1] >= 0:
                            antinodes.add(coord)

        return len(antinodes)

    def unique_locations_part2(self, inp: str):
        grid = []
        lines = inp.splitlines()
        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        antennas = {}
        antinodes = set()
        
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] != '.':
                    antennas.setdefault(grid[row_i][col_i], [])
                    antennas[grid[row_i][col_i]].append((row_i, col_i))

        for k, antenna_block in antennas.items():
            n_b = len(antenna_block)

            if n_b < 2:
                continue

            for i in range(n_b):
                antinodes.add(antenna_block[i])

            for i in range(n_b):
                for j in range(i + 1, n_b):
                    for pair in [(antenna_block[i], antenna_block[j]), (antenna_block[j], antenna_block[i])]:
                        diff = tuple(map(operator.sub, pair[1], pair[0]))
                        pos = pair[0]
                        while n_rows > pos[0] >= 0 and n_cols > pos[1] >= 0:
                            antinodes.add(pos)
                            pos = tuple(map(operator.sub, pos, diff))

                        pos = pair[1]
                        while n_rows > pos[0] >= 0 and n_cols > pos[1] >= 0:
                            antinodes.add(pos)
                            pos = tuple(map(operator.add, pos, diff))


        return len(antinodes)
