# 1010번 다리놓기
# M개 중 N개를 고르면 답 -> mCn = mPn/n!

num = int(input())

for i in range(num):
    n, m = map(int, input().split())

    a, b = 1, 1
    for j in range(n): # 0 1 2 ... n-1
        a *= (m-j) # m m-1 m-2 ...
        b *= (j+1) # 1 2 3 ... n
    
    print(a//b)