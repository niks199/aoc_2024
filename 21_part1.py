from functools import cache
import sys

class Solution:
    def sum_of_complexites(self, inp: str):
        sys.setrecursionlimit(14500000)
        c = 0
        for code in inp.splitlines():
            print(f'solve {code}')
            num = int(code[:3])
            cache = {}
            v = self.all_combs(code, 'A', '', cache)
            c += num * v
        return c
      
    @cache
    def navpad_to_navpad(self, prev_mark, next_mark):
        n_r = 2
        n_c = 3
        gap = (0, 0)

        navpad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
        navpad_to_mark = {}

        parents = {}
        distances = {}

        for mark, pos in navpad.items():
            navpad_to_mark[pos] = mark
            parents[mark] = []
            distances[mark] = float('inf')
        
        distances[prev_mark] = 0
        parents[prev_mark] = [-1]

        nav_moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

        q = [(prev_mark, [], [prev_mark])]

        while q:
            (mark, mark_path, path) = q.pop(0)
            
            pos = navpad[mark]

            for sign, m in nav_moves.items():
                n_pos = (pos[0] + m[0], pos[1] + m[1])

                if n_pos[0] < 0 or n_pos[0] >= n_r or n_pos[1] < 0 or n_pos[1] >= n_c:
                    continue
                if n_pos == gap:
                    continue
                if navpad_to_mark[n_pos] in path:
                    continue
                if distances[navpad_to_mark[n_pos]] > distances[navpad_to_mark[pos]] + 1:
                    distances[navpad_to_mark[n_pos]] = distances[navpad_to_mark[pos]] + 1
                    q.append((navpad_to_mark[n_pos], mark_path + [sign], path + [navpad_to_mark[n_pos]]))
                    parents[navpad_to_mark[n_pos]].clear()
                    parents[navpad_to_mark[n_pos]].append((navpad_to_mark[pos], sign))
                elif distances[navpad_to_mark[n_pos]] == distances[navpad_to_mark[pos]] + 1:
                    parents[navpad_to_mark[n_pos]].append((navpad_to_mark[pos], sign))

        paths = []

        self.find_paths(parents, (next_mark, 'A'), [], paths)

        return paths

    @cache
    def numpad_to_navpad(self, prev_d, next_d):
        numpad = {'A': (3, 2), '0': (3, 1), '1': (2, 0), 
                  '2': (2, 1), '3': (2, 2), '4': (1, 0), 
                  '5': (1, 1), '6': (1, 2), '7': (0, 0),
                  '8': (0, 1), '9': (0, 2)}
        
        pos_to_num = {}

        parents = {}
        distances = {}

        for d, pos in numpad.items():
            pos_to_num[pos] = d
            parents[d] = []
            distances[d] = float('inf')
        
        nav_moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

        parents[prev_d] = [-1]
        distances[prev_d] = 0

        q = [(prev_d, [], [prev_d])]

        n_r = 4
        n_c = 3
        gap = (3, 0)

        while q:
            (num_d, nav_list, path) = q.pop(0)
            
            pos = numpad[num_d]

            for sign, move in nav_moves.items():
                n_pos = (pos[0] + move[0], pos[1] + move[1])

                if n_pos[0] < 0 or n_pos[0] >= n_r or n_pos[1] < 0 or n_pos[1] >= n_c:
                    continue
                if n_pos == gap:
                    continue
                if pos_to_num[n_pos] in path:
                    continue

                if distances[pos_to_num[n_pos]] > distances[pos_to_num[pos]] + 1:
                    distances[pos_to_num[n_pos]] = distances[pos_to_num[pos]] + 1
                    q.append((pos_to_num[n_pos], nav_list + [sign], path + [pos_to_num[n_pos]]))
                    parents[pos_to_num[n_pos]].clear()
                    parents[pos_to_num[n_pos]].append((pos_to_num[pos], sign))
                elif distances[pos_to_num[n_pos]] == distances[pos_to_num[pos]] + 1:
                    parents[pos_to_num[n_pos]].append((pos_to_num[pos], sign))

        paths = []
        self.find_paths(parents, (next_d, 'A'), [], paths)
        return paths

    def find_paths(self, parents, dest, path, paths):
        if dest == -1:
            path_copy = path[:]
            path_copy.reverse()
            paths.append(''.join(path_copy))
            return
        
        for parent in parents[dest[0]]:
            path.append(dest[1])
            self.find_paths(parents, parent, path, paths)
            path.pop()

    def all_navpad_3(self, code, prev_button, instr, cache):
        key = (code, prev_button)
        if key not in cache:
            if len(code) == 0:
                return len(instr)

            navpad_paths = sol.navpad_to_navpad(prev_button, code[0])

            min_l = float('inf')

            for navpad_path in navpad_paths:
                v = self.all_navpad_3(code[1:], code[0], instr + navpad_path, cache)
                min_l = min(min_l, v)
            
            cache[key] = min_l
        return cache[key]

    def all_navpad_2(self, code, prev_button, instr, cache):
        key = (code, prev_button, instr)
        if key not in cache:
            if len(code) == 0:
                sub_cache = {}
                return self.all_navpad_3(instr, 'A', '', sub_cache)

            navpad_paths = sol.navpad_to_navpad(prev_button, code[0])

            min_l = float('inf')
            for navpad_path in navpad_paths:
                v = self.all_navpad_2(code[1:], code[0], instr + navpad_path, cache)
                min_l = min(min_l, v)
            
            cache[key] = min_l
        return cache[key]

    def all_combs(self, code, prev_button, instr, cache):
        key = (code, prev_button, instr)
        if key not in cache:
            if len(code) == 0:
                sub_cache = {}
                return self.all_navpad_2(instr, 'A', '', sub_cache)
            
            navpad_one_paths = sol.numpad_to_navpad(prev_button, code[0])

            min_l = float('inf')
            for navpad_one_path in navpad_one_paths:
                v = self.all_combs(code[1:], code[0], instr + navpad_one_path, cache)
                min_l = min(min_l, v)

            cache[key] = min_l
        return cache[key]
