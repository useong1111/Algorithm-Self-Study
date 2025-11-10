# 1676번 팩토리얼 0의 개수
# 걍 무식하게 해야겠는데??

n = int(input())

n_factorial = 1
ret = 0

for i in range(1, n+1): n_factorial *= i

while True:
    if n_factorial % 10:
        break
    else:
        ret += 1
        n_factorial //= 10

print(ret)