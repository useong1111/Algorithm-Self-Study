# 1181번 단어 정렬

# 길이별로 다른 list에 넣기
# 하나의 list에 넣고 sort key를 len으로 해도 될듯?
# sorted_list = sorted(input_list, key= lambda x : (len(x), x))

from collections import defaultdict

word_dict = defaultdict(set)
n = int(input())
for _ in range(n):
    input_word = input()
    input_len = len(input_word)
    word_dict[input_len].add(input_word)

for i in range(1, 51):
    if len(word_dict[i]) == 0: continue
    for j in sorted(list(word_dict[i])): print(j)