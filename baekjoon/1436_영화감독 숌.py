# 1436번 영화감독 숌

# 다른 코드들 보니, for '666' in str(i)와 같이 연산하는게 훨씬 빠르네

def isDoomNum(num):
    six_count = 0
    while num:
        modulo = num % 10
        if modulo == 6: six_count += 1
        else: six_count = 0
        num = num // 10

        if six_count == 3: return True

    return False

n = int(input())
doomNumList = []

for i in range(666, 2700000):
    if isDoomNum(i): doomNumList.append(i)

print(doomNumList[n-1])