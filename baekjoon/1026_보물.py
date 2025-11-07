# 1026번 보물

# 모든 원소는 0-99 사이 정수
# 모든 경우의 수를 계산하면? 시간 초과일듯 확실히

# 큰 거끼리 곱하면 숫자가 폭발할거 아냐?
# 그러면 큰거 * 작은거 이런 식으로 해야하나? 그러려면 서로 반대로 정렬해서 곱하기?

n = int(input())
list_a = [int(x) for x in map(int, input().split())]
list_b = [int(x) for x in map(int, input().split())]

ret = 0

for a, b in zip(sorted(list_a), sorted(list_b, reverse=True)):
    ret += a*b

print(ret)