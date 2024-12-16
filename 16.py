import operator
import heapq
import sys

class Solution:
    def lowest_score(self, inp: str):
        lines = inp.splitlines()

        grid = []

        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        grid_bounds = [[1, n_rows - 2], [1, n_cols - 2]]

        adj_list = {}

        dirs = ['N', 'E', 'S', 'W']
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row_i in range(1, n_rows - 1):
            for col_i in range(1, n_cols - 1):
                if grid[row_i][col_i] == '#':
                    continue

                for i in range(4):
                    t = ((row_i, col_i), dirs[i])
                    adj_list.setdefault(t, set())
                    neigh_pos = tuple(map(operator.add, t[0], moves[i]))

                    if all((grid_bounds[i_b][1] >= neigh_pos[i_b] >= grid_bounds[i_b][0]) for i_b in [0, 1]) and \
                        grid[neigh_pos[0]][neigh_pos[1]] != '#':
                        neigh_t = (neigh_pos, dirs[(i + 2) % 4])
                        adj_list[t].add((neigh_t, 1))

                        adj_list.setdefault(neigh_t, set())
                        adj_list[neigh_t].add((t, 1))
                
                for i in range(1, 5):
                    u = ((row_i, col_i), dirs[(i - 1) % 4])
                    adj_list.setdefault(u, set())
                    v = ((row_i, col_i), dirs[(i) % 4])
                    adj_list[u].add((v, 1000))
                    adj_list.setdefault(v, set())
                    adj_list[v].add((u, 1000))
                
                u = ((row_i, col_i), dirs[0])
                v = ((row_i, col_i), dirs[2])

                adj_list[u].add((v, 0))
                adj_list[v].add((u, 0))

                u = ((row_i, col_i), dirs[1])
                v = ((row_i, col_i), dirs[3])

                adj_list[u].add((v, 0))
                adj_list[v].add((u, 0))

        s = None
        e = None
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == 'S':
                    s = ((row_i, col_i), 'E')
                elif grid[row_i][col_i] == 'E':
                    e = ((row_i, col_i), 'S')
        v = {}

        for k in adj_list.keys():
            v[k] = float('inf')

        v[s] = 0

        pq = []
        heapq.heappush(pq, (v[s], s))

        prev = {}

        while pq:
            (dist, vert) = heapq.heappop(pq)

            for neigh in adj_list[vert]:
                dist_via_vert = dist + neigh[1]
                if dist_via_vert < v[neigh[0]]:
                    v[neigh[0]] = dist_via_vert
                    prev[neigh[0]] = vert
                    heapq.heappush(pq, (dist_via_vert, neigh[0]))


        ans = v[e]

        path = []
        u = e
        while u in prev:
            path.insert(0, u)
            u = prev[u]

        path.insert(0, s)

        
        #print(path)

        unique_tiles = set()
        for p in path:
            unique_tiles.add(p[0])

        print(len(unique_tiles))
        return ans

    def lowest_score_part2(self, inp: str):
        sys.setrecursionlimit(1450000)
        lines = inp.splitlines()

        grid = []

        for line in lines:
            grid.append(list(line))

        n_rows = len(grid)
        n_cols = len(grid[0])

        grid_bounds = [[1, n_rows - 2], [1, n_cols - 2]]

        adj_list = {}

        dirs = ['N', 'E', 'S', 'W']
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row_i in range(1, n_rows - 1):
            for col_i in range(1, n_cols - 1):
                if grid[row_i][col_i] == '#':
                    continue

                for i in range(4):
                    t = ((row_i, col_i), dirs[i])
                    adj_list.setdefault(t, set())
                    neigh_pos = tuple(map(operator.add, t[0], moves[i]))

                    if all((grid_bounds[i_b][1] >= neigh_pos[i_b] >= grid_bounds[i_b][0]) for i_b in [0, 1]) and \
                        grid[neigh_pos[0]][neigh_pos[1]] != '#':
                        neigh_t = (neigh_pos, dirs[(i + 2) % 4])
                        adj_list[t].add((neigh_t, 1))

                        adj_list.setdefault(neigh_t, set())
                        adj_list[neigh_t].add((t, 1))
                
                for i in range(1, 5):
                    u = ((row_i, col_i), dirs[(i - 1) % 4])
                    adj_list.setdefault(u, set())
                    v = ((row_i, col_i), dirs[(i) % 4])
                    adj_list[u].add((v, 1000))
                    adj_list.setdefault(v, set())
                    adj_list[v].add((u, 1000))
                
                u = ((row_i, col_i), dirs[0])
                v = ((row_i, col_i), dirs[2])

                adj_list[u].add((v, 0.000001))
                adj_list[v].add((u, 0.000001))

                u = ((row_i, col_i), dirs[1])
                v = ((row_i, col_i), dirs[3])

                adj_list[u].add((v, 0.000001))
                adj_list[v].add((u, 0.000001))

        s = None
        e = None
        for row_i in range(n_rows):
            for col_i in range(n_cols):
                if grid[row_i][col_i] == 'S':
                    s = ((row_i, col_i), 'E')
                elif grid[row_i][col_i] == 'E':
                    e = ((row_i, col_i), 'S')
        v = {}

        for k in adj_list.keys():
            v[k] = float('inf')

        v[s] = 0

        pq = []
    
        heapq.heappush(pq, (v[s], s))

        prev = {}

        while pq:
            (dist, vert) = heapq.heappop(pq)

            for neigh in adj_list[vert]:
                dist_via_vert = dist + neigh[1]
                if dist_via_vert <= v[neigh[0]]:
                    prev.setdefault(neigh[0], set())
                    if dist_via_vert < v[neigh[0]]:
                        v[neigh[0]] = dist_via_vert
                        prev[neigh[0]].clear()
                    prev[neigh[0]].add(vert)
                    heapq.heappush(pq, (dist_via_vert, neigh[0]))

        tiles = set()

        self.dfs2(prev, e, tiles)

        for tile in tiles:
           grid[tile[0]][tile[1]] = 'O'
        
        #self.print_grid(grid)
        return len(tiles)
    
    def dfs2(self, prev, v, tiles):
        tiles.add(v[0])
        if v in prev:
            for v_next in prev[v]:
                self.dfs2(prev, v_next, tiles)

    def print_grid(self, grid):
        s = "\n".join([str(g) for g in grid])
        print(s)
        print()
        print()
