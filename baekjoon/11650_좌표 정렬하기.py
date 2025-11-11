# 11650번 좌표 정렬하기
# python sort, sorted - 안정 정렬, O(n log n)

import sys
input = sys.stdin.readline

dot_list = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    dot_list.append((x, y))

dot_list.sort(key=lambda a: (a[0], a[1]))

for x, y in dot_list: print(x, y)