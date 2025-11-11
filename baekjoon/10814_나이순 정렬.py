# 10814번 나이순 정렬
# python sort, sorted - 안정 정렬, O(n log n)

import sys
input = sys.stdin.readline

mem_list = []

n = int(input())
for _ in range(n):
    age, name = input().split()
    mem_list.append((int(age), name))

mem_list.sort(key=lambda x: x[0])

for age, name in mem_list: print(age, name)