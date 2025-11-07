# 1049번 기타줄

# 6개 패키지 가격의 min값과 1개 가격 min값을 구해두고,
# min(6개 패키지로만 사기, 6개 패키지로 사고 나머지만 1개로 사기, 1개로만 사기)
# 1개로만 사는 것은 왜 있나? 6개 패키지 가격이 1개 가격 * 6보다 꼭 저렴하다는 보장이 없다

n, m = map(int, input().split())
min_6, min_1 = 10000, 10000

for i in range(m):
    price_6, price_1 = map(int, input().split())

    if price_6 < min_6: min_6 = price_6
    if price_1 < min_1: min_1 = price_1

need_6 = n//6
if n%6 != 0: need_6 += 1

print(min(n * min_1, n//6 * min_6 + n%6 * min_1, need_6 * min_6))