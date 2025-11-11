# 4153번 직각삼각형

import sys
input = sys.stdin.readline

while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0 and b == 0 and c == 0: break
    elif a ** 2 + b ** 2 == c ** 2: print('right')
    else: print('wrong')