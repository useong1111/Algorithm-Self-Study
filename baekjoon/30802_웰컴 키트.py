# 30802번 웰컴 키트
# divmod(a, b) = a//b, a%b

import sys
input = sys.stdin.readline

n = int(input())
sizes = [int(_) for _ in map(int, input().split())]
t, p = map(int, input().split())

t_bundle_cnt = 0
for size in sizes:
    a, b = divmod(size, t)
    if b == 0: t_bundle_cnt += a
    else: t_bundle_cnt += (a+1)

a, b = divmod(n, p)

print(t_bundle_cnt)
print(a, b)