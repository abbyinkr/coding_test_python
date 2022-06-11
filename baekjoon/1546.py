n = int(input())
score_list = list(map(int, input().split()))

M = max(score_list)

for i in range(len(score_list)):
  score_list[i] = score_list[i] / M * 100

print(sum(score_list)/len(score_list))


