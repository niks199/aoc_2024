import re
import sys

class Solution:
    def possible_designs(self, inp: str):
        pattern1 = "(\w+)[^,]?+"

        lines = inp.splitlines()

        towel_patterns = []

        result = re.findall(pattern1, lines[0])
        for r in result:
            towel_patterns.append(r)
        
        designs = []

        for i in range(2, len(lines)):
            designs.append(lines[i])

        count = 0
        for i, design in enumerate(designs):
            print(f'desgin {i} {design} {len(design)}')
            seen = set()
            if self.possible_design(design, towel_patterns, 0, '', seen):
                count += 1
            print(f'count {count}')
        return count

    def possible_design(self, design: str, towel_patterns, d_i, current_towel, seen):
        n = len(design)

        if d_i == n:
            return True
        
        if d_i > n:
            return False

        n_t = len(towel_patterns)

        for t_i in range(n_t):
            tup = (current_towel, d_i, t_i)

            if tup in seen:
                continue

            seen.add(tup)
        
            if design.startswith(towel_patterns[t_i], d_i):
                if self.possible_design(design, 
                                    towel_patterns, 
                                    d_i + len(towel_patterns[t_i]), 
                                    current_towel + towel_patterns[t_i],
                                    seen):
                    return True

        return False

    def number_of_different_ways_hint(self, inp: str):
        sys.setrecursionlimit(14500000)
        pattern1 = "(\w+)[^,]?+"

        lines = inp.splitlines()

        towel_patterns = []

        result = re.findall(pattern1, lines[0])
        for r in result:
            towel_patterns.append(r)
        
        designs = []

        for i in range(2, len(lines)):
            designs.append(lines[i])

        self.towel_patterns = towel_patterns

        c = 0
        for design in designs:
            cache = {}
            c += self.count_for_design2(design, cache)
        return c

    def count_for_design2(self, design, cache):
        if design not in cache:
            if not design:
                return 1
            
            res = 0
            for t in self.towel_patterns:
                if design.startswith(t):
                    res += self.count_for_design2(design[len(t):], cache)
            cache[design] = res
        return cache[design]
