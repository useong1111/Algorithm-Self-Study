# 1259번 팰린드롬수
# 수(int) 차원이 아니라 문자열(str) 차원에서 하면 되겠네

while True:
    n = input()
    if n == '0': break

    if n == n[::-1]: print('yes')
    else: print('no')