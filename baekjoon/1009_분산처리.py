# 1009번 분산처리
# a**b % 10 하면 간단한데? 근데 99**999999 % 10이 계산될까?
# 안되네; 에러난다!

# 결국 중요한건 1의 자리..
# 그리고 b번 제곱을 진짜하면 에러날듯

t = int(input())
div_list = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]

for i in range(t):
    a, b = map(int, input().split())
    if a % 10 == 0: print(10)
    else:
        a %= 10
        b = b % div_list[a]
        if b == 0: b = div_list[a]
        print(a ** b % 10)