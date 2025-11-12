# 11866번 요세푸스 문제 0

# deque 사용 - 계속 순환하니까 popleft -> append 하는게 편하겠다
# 출력 - 문자열로 만드는게 편하겠다

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque(range(1, n+1))
ret = []

while deq:
    for _ in range(k-1): deq.append(deq.popleft())
    ret.append(deq.popleft())

print("<", str(ret)[1:-1], ">", sep = "")