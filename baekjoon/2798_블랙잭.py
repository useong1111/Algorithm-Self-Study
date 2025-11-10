# 2798번 블랙잭
# 다 계산해버리기~

from itertools import combinations

n, m = map(int, input().split())
ret = -1

nums = [int(_) for _ in map(int, input().split())]

for i in (combinations(nums, 3)):
    if ret < sum(i) <= m: ret = sum(i)

print(ret)