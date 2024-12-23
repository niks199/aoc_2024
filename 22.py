import math
import sys
from functools import cache

def secret_value_calc(secret: int):
    v = secret * 64

    secret = v ^ secret
    secret = secret % 16777216
    v2 = math.floor(secret / 32)
    secret = v2 ^ secret
    secret = secret % 16777216

    v3 = secret * 2048
    secret = v3 ^ secret

    secret = secret % 16777216

    return secret

def secret_value_part1(secret: int, num_values: int):
    for i in range(num_values):
        secret = secret_value_calc(secret)

    return secret

def sum_of_secrets(inp: str, num: int):
    sys.setrecursionlimit(14500000)
    return sum([secret_value_part1(int(secret), num) for secret in inp.splitlines()])


def most_bananas(inp: str, num_values: int):
    secrets = [int(secret) for secret in inp.splitlines()]

    all_patterns = {}
    for s_i, secret in enumerate(secrets):
        print(f'processing {s_i} of {len(secrets)} {secret}')
        secret_patterns = pattern_bananas(secret, num_values)
        for pattern, price in secret_patterns.items():
            all_patterns.setdefault(pattern, 0)
            all_patterns[pattern] += price

    max_v = 0
    for pattern, v in all_patterns.items():
        max_v = max(max_v, v)
    
    return max_v

def pattern_bananas(secret: int, num_values: int):
    secrets = []

    for i in range(num_values):
        secrets.append(secret)
        secret = secret_value_calc(secret)

    prices = [int(str(s)[-1]) for s in secrets]

    d = [a - b for (a, b) in zip(prices[1:], prices)]

    patterns = {}

    price_patterns = [pp for pp in zip(d, d[1:], d[2:], d[3:], prices[4:])]

    for price_pattern in price_patterns:
         pattern = tuple(price_pattern[:4])
         if pattern in patterns:
             continue
         if price_pattern[-1] == 0:
             continue
         patterns[pattern] = price_pattern[-1]

    return patterns
