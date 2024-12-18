import re
import math

class Solution:
    def device_values(self, inp: str):
        pattern1 = "Register A: ([0-9]+)"
        pattern2 = "Register B: ([0-9]+)"
        pattern3 = "Register C: ([0-9]+)"

        pattern4 = "Program: ([0-9](,[0-9])*)"

        lines = inp.splitlines()

        debugger = {}

        results = re.findall(pattern1, lines[0])
        debugger['register_a'] = int(results[0])
        results = re.findall(pattern2, lines[1])
        debugger['register_b'] = int(results[0])
        results = re.findall(pattern3, lines[2])
        debugger['register_c'] = int(results[0])
        results = re.findall(pattern4, lines[4])
        debugger['program'] = [int(v)for v in results[0][0].split(',')]

        n = len(debugger['program'])

        l = 0

        ops = {0: 'adv', 1: 'bxl', 2: 'bst', 3: 'jnz', 4: 'bxc', 5: 'out', 6: 'bdv', 7: 'cdv'}

        output = ''

        while l < n - 1:
            opcode = debugger['program'][l]

            instruction = ops[opcode]

            print(f'instruxtion {instruction}')

            if instruction == 'adv':
                numerator = debugger['register_a']
                denominator = math.pow(2, self.combo_operand(debugger, debugger['program'][l + 1]))
                result = numerator / denominator
                debugger['register_a'] = int(result)
                l += 2
            elif instruction == 'bxl':
                result = debugger['register_b'] ^ debugger['program'][l + 1]
                debugger['register_b'] = result
                l += 2
            elif instruction == 'bst':
                result = self.combo_operand(debugger, debugger['program'][l + 1]) % 8
                debugger['register_b'] = result
                l += 2
            elif instruction == 'jnz':
                if debugger['register_a'] == 0:
                    l += 2
                else:
                    literal_operand = debugger['program'][l + 1]
                    l = literal_operand
                print(f"rega {debugger['register_a'] }")
            elif instruction == 'bxc':
                result = debugger['register_b'] ^ debugger['register_c']
                debugger['register_b'] = result
                l += 2
            elif instruction == 'out':
                result = self.combo_operand(debugger, debugger['program'][l + 1]) % 8
                if not output:
                    output = f'{result}'
                else:
                    output += f',{result}'
                l += 2
                print(f'res {result}')
            elif instruction == 'bdv':
                numerator = debugger['register_a']
                denominator = math.pow(2, self.combo_operand(debugger, debugger['program'][l + 1]))
                result = numerator / denominator
                debugger['register_b'] = int(result)
                l += 2
            elif instruction == 'cdv':
                numerator = debugger['register_a']
                denominator = math.pow(2, self.combo_operand(debugger, debugger['program'][l + 1]))
                result = numerator / denominator
                debugger['register_c'] = int(result)
                l += 2

        return output

    def combo_operand(self, debugger, operand):
        if 3 >= operand >= 0:
            return operand
        elif operand == 4:
            return debugger['register_a']
        elif operand == 5:
            return debugger['register_b']
        elif operand == 6:
            return debugger['register_c']
        else:
            print('error')
        return -1
    
    def device_values_part2_rev2(self, inp):
        """Register A: 21539243
Register B: 0
Register C: 0

Program: 2,4,1,3,7,5,1,5,0,3,4,1,5,5,3,0
"""
        pattern4 = "Program: ([0-9](,[0-9])*)"

        lines = inp.splitlines()

        debugger = {}

        debugger['register_a'] = 0
        debugger['register_b'] = 0
        debugger['register_c'] = 0
        results = re.findall(pattern4, lines[4])
        debugger['program'] = [int(v)for v in results[0][0].split(',')]

# 1. bst - 2
#    reg_b = reg_a % 8 
# 2. bxl - 1
#    reg_b = reg_b ^ 3
# 3. 7 - cdv
#    reg_c = reg_a >> reg_b or reg_a / (2 << reg_b)
# 4. 1 - bxl
#    reg_b = reg_b ^ 5
# 5. 0 - adv
#    reg_a = reg_a >> 3 or reg_a / (2 << 3)
# 6. 4 - bxc
#    reg_b = reg_b ^ reg_c
# 7. 5 - out
#    print reg_b % 8
# 8. 3 - jnz
#    if reg_a == 0:
#        nothing
#    else:
#        jump to 0 % 8

# reverse engineer the program:
# then try different value for reg_a to get the single output.
# moving backwards over the program items

# reg_a = 8 + []

# reg_b = reg_a % 8
# reg_b = reg_b ^ 3
# reg_c = reg_a >> reg_b
# reg_b = reg_b ^ 5
# reg_a = reg_a >> 3
# reg_b = reg_b ^ reg_c
# print reg_b % 8
# if reg_a != 0:
#    jump to 0 % 8

        return self.find(debugger['program'], 0)

    def find(self, prog, ans):
        if not prog:
            return ans
        for reg_b in range(8):
            reg_a = (ans << 3) + reg_b
            reg_b = reg_b ^ 3
            reg_c = reg_a >> reg_b
            reg_b = reg_b ^ 5
            #reg_a = reg_a >> 3
            reg_b = reg_b ^ reg_c
            if reg_b % 8 == prog[-1]:
                sub = self.find(prog[:-1], reg_a)
                if not sub:
                    continue
                
                return sub
