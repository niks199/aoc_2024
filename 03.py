import re
class Solution:
    def multiplications(self, s: str):
        #/(?<![x,_])mul\([0-9]{1,3}\,[0-9]{1,3}\)/gm
        #"/mul\([0-9]{1,3}\,[0-9]{1,3}\)/gm"

        pattern1 = "mul\(([0-9]{1,3})\,([0-9]{1,3})\)"

        results = re.findall(pattern1, s)

        tot = 0
        for res in results:
            tot += int(res[0]) * int(res[1])
            print(res[1])

        return tot
    
    def multiplications_instructions(self, s: str):
        pattern1 = "mul\(([0-9]{1,3})\,([0-9]{1,3})\)"
        pattern2 = "do\(\)"
        pattern3 = "don't\(\)"

        pattern = f'({pattern1})|({pattern2})|({pattern3})'

        results = re.findall(pattern, s)

        tot = 0
        enabled = True
        for res in results:
            if res[3]:
                enabled = True
            elif res[4]:
                enabled = False
            elif res[1] and res[2]:
                if enabled:
                    tot += int(res[1]) * int(res[2])

        return tot
