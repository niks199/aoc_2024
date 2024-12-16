import re

class Solution:
    def safety_factor(self, inp: str, n_rows: int, n_cols: int):
        pattern = '(p=([0-9]+),([0-9]+) v=([-]{0,1}[0-9]+),([-]{0,1}[0-9]+))'

        lines = inp.splitlines()

        robots = []

        # x, y
        for line in lines:
            results = re.findall(pattern, line)
            pos = (int(results[0][1]), int(results[0][2]))
            velocity = (int(results[0][3]), int(results[0][4]))
            robot = {'pos': pos, 'velocity': velocity}
            robots.append(robot)

        seconds = 100

        for _ in range(seconds):
            for i, robot in enumerate(robots):
                n_pos = ((robot['pos'][0] + robot['velocity'][0]) % n_cols, (robot['pos'][1] + robot['velocity'][1]) % n_rows)
                robots[i]['pos'] = n_pos

        m_v = n_cols // 2
        m_h = n_rows // 2

        q = [0] * 4

        relevant = 0
        for robot in robots:
            if robot['pos'][0] == m_v or robot['pos'][1] == m_h:
                continue
            if m_h > robot['pos'][1] >= 0:
                if m_v > robot['pos'][0] >= 0:
                    q[0] += 1
                else:
                    q[1] += 1
            else:
                if m_v > robot['pos'][0] >= 0:
                    q[2] += 1
                else:
                    q[3] += 1

            relevant += 1
        
        non_r = len(robots) - relevant

        r = q[0] * q[1] * q[2] * q[3]

        return r

    def easter_egg(self, inp: str, n_rows: int, n_cols: int):
        pattern = '(p=([0-9]+),([0-9]+) v=([-]{0,1}[0-9]+),([-]{0,1}[0-9]+))'

        lines = inp.splitlines()

        robots = []

        # x, y
        for line in lines:
            results = re.findall(pattern, line)
            pos = (int(results[0][1]), int(results[0][2]))
            velocity = (int(results[0][3]), int(results[0][4]))
            robot = {'pos': pos, 'velocity': velocity}
            robots.append(robot)

        seconds = 0

        min_f = float('inf')
        while True:
            for i, robot in enumerate(robots):
                n_pos = ((robot['pos'][0] + robot['velocity'][0]) % n_cols, (robot['pos'][1] + robot['velocity'][1]) % n_rows)
                robots[i]['pos'] = n_pos

            seconds += 1
            f = self.factor(robots, n_rows, n_cols)
            if f < min_f:
                min_f = f
                # looked for the hint: idea is egg is located only in single quadrant, opposite to chrismas tree
                # waiting until no more min factor
                print(f'mf {min_f} seconds {seconds}')


    def factor(self, robots, n_rows, n_cols):
        m_v = n_cols // 2
        m_h = n_rows // 2

        q = [0] * 4

        relevant = 0
        for robot in robots:
            if robot['pos'][0] == m_v or robot['pos'][1] == m_h:
                continue
            if m_h > robot['pos'][1] >= 0:
                if m_v > robot['pos'][0] >= 0:
                    q[0] += 1
                else:
                    q[1] += 1
            else:
                if m_v > robot['pos'][0] >= 0:
                    q[2] += 1
                else:
                    q[3] += 1

            relevant += 1
        
        non_r = len(robots) - relevant

        r = q[0] * q[1] * q[2] * q[3]

        return r
