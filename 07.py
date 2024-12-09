class Solution:
    def calibration_result(self, inp: str):
        inp.strip
        lines = inp.splitlines()
        equations = []
        for line in lines:
            items = line.split(':')
            result = int(items[0])
            items[1] = items[1].strip()
            parts = [int(part.strip()) for part in items[1].split(' ')]

            equations.append([result, parts])

        tot = 0
        for equation in equations:
            if self.solve2(equation, 1, equation[1][0]):
                tot += equation[0]
        return tot

    def solve2(self, eq, p_i, cur):
        n = len(eq[1])

        if p_i == n:
            if cur == eq[0]:
                return True
            return False

        for oper in ['+', '*']:
            res = self.solve2(eq, p_i + 1, self.oper_impl(cur, eq[1][p_i], oper))
            if res:
                return True

        return False

    def oper_impl(self, a, b, oper):
        if b == -1:
            return a
        if oper == '+':
            return a + b
        else:
            return a * b

    def calibration_result_part2(self, inp: str):
        inp.strip
        lines = inp.splitlines()
        equations = []
        for line in lines:
            items = line.split(':')
            result = int(items[0])
            items[1] = items[1].strip()
            parts = [int(part.strip()) for part in items[1].split(' ')]

            equations.append([result, parts])

        tot = 0
        for equation in equations:
            if self.solve_part2(equation, 1, equation[1][0]):
                tot += equation[0]
        return tot

    def solve_part2(self, eq, p_i, cur):
        n = len(eq[1])

        if p_i == n:
            if cur == eq[0]:
                return True
            return False

        for oper in ['+', '*', '||']:
            res = self.solve_part2(eq, p_i + 1, self.oper_impl_part2(cur, eq[1][p_i], oper))
            if res:
                return True

        return False

    def oper_impl_part2(self, a, b, oper):
        if b == -1:
            return a
        if oper == '+':
            return a + b
        elif oper == '*':
            return a * b
        else:
            return int(str(a)+str(b))
