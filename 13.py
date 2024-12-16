import re

class Solution:
    def fewest_tokens(self, inp: str):
        pattern1 = '(Button A: X\+([0-9]+), Y\+([0-9]+))'
        pattern2 = '(Button B: X\+([0-9]+), Y\+([0-9]+))'
        pattern3 = '(Prize: X=([0-9]+), Y=([0-9]+))'

        pattern = f'({pattern1})|({pattern2})|({pattern3})'

        lines = inp.splitlines()
        pattern_id = 0

        button_a = {}
        button_b = {}
        prize = {}

        claws = []

        for line in lines:
            if line:
                results = re.findall(pattern, line)
                if pattern_id == 0:
                    x = results[0][2]
                    y = results[0][3]
                    button_a = {'x': int(x), 'y': int(y)}
                elif pattern_id == 1:
                    x = results[0][6]
                    y = results[0][7]
                    button_b = {'x': int(x), 'y': int(y)}
                if pattern_id == 2:
                    x = results[0][10]
                    y = results[0][11]
                    prize = {'x': int(x), 'y': int(y)}
                    claws.append((button_a, button_b, prize))
                pattern_id = (pattern_id + 1) % 3

        tot = 0
        for i, claw in enumerate(claws):
            dp = {}
            v = self.tokens_for_claw(claw, 0, 0, 0, 0, dp)
            if v != float('inf'):
                tot += v

        return tot

    def tokens_for_claw(self, claw, presses_a, presses_b, pos_x, pos_y, dp):
        t = (presses_a, presses_b, pos_x, pos_y)
        if t in dp:
            return dp[t]
        
        if presses_a == 101 or presses_b == 101:
            dp[t] = float('inf')
            return float('inf')
        
        if pos_x > claw[2]['x']:
            dp[t] = float('inf')
            return float('inf')
        if pos_y > claw[2]['y']:
            dp[t] = float('inf')
            return float('inf')

        if pos_x == claw[2]['x'] and pos_y == claw[2]['y']:
            r = presses_a * 3 + presses_b * 1
            dp[t] = float('inf')
            return r

        v1 = self.tokens_for_claw(claw, presses_a + 1, presses_b, pos_x + claw[0]['x'], pos_y + claw[0]['y'], dp)
        v2 = self.tokens_for_claw(claw, presses_a, presses_b + 1, pos_x + claw[1]['x'], pos_y + claw[1]['y'], dp)
        
        r = min(v1, v2)

        dp[t] = r
        return r

    def fewest_tokens_part2(self, inp: str):
        pattern1 = '(Button A: X\+([0-9]+), Y\+([0-9]+))'
        pattern2 = '(Button B: X\+([0-9]+), Y\+([0-9]+))'
        pattern3 = '(Prize: X=([0-9]+), Y=([0-9]+))'

        pattern = f'({pattern1})|({pattern2})|({pattern3})'

        lines = inp.splitlines()
        pattern_id = 0

        button_a = {}
        button_b = {}
        prize = {}

        claws = []

        for line in lines:
            if line:
                results = re.findall(pattern, line)
                if pattern_id == 0:
                    x = results[0][2]
                    y = results[0][3]
                    button_a = {'x': int(x), 'y': int(y)}
                elif pattern_id == 1:
                    x = results[0][6]
                    y = results[0][7]
                    button_b = {'x': int(x), 'y': int(y)}
                if pattern_id == 2:
                    x = results[0][10]
                    y = results[0][11]
                    prize = {'x': int(x) + 10000000000000, 'y': int(y) + 10000000000000}
                    claws.append((button_a, button_b, prize))
                pattern_id = (pattern_id + 1) % 3

        tot = 0
        for i, claw in enumerate(claws):
            v = self.tokens_for_claw_part2(claw)
            if v != float('inf'):
                tot += v
            print(f'i {i} - {v}')

        return tot

    def tokens_for_claw_part2(self, claw):
        # looked for the hint
        # A*a_x + B*b_x = p_x
        # A*a_y + B*b_y = p_y

        a_x = claw[0]['x']
        a_y = claw[0]['y']
        b_x = claw[1]['x']
        b_y = claw[1]['y']
        p_x = claw[2]['x']
        p_y = claw[2]['y']

        A = (p_x*b_y - p_y*b_x) / (a_x*b_y - a_y*b_x)
        B = (a_x*p_y - a_y*p_x) / (a_x*b_y - a_y*b_x)
        A = int(A)
        B= int(B)

        if A * a_x + B * b_x == p_x and A * a_y + B * b_y == p_y:
            return A * 3 + B
        else:
            return 0
