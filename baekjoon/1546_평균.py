# 1546번 평균
# 기존 평균 / 최댓값

n = int(input())
scores = [int(_) for _ in map(int, input().split())]

print(100*sum(scores)/len(scores)/max(scores))