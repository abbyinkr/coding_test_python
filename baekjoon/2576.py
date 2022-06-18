N = 7
number_list = []
# 홀수 합
odd_sum = 0

# 0 ~ 6 : 총 7번
for i in range(N):
    num = int(input())
    if num % 2 == 1:
      number_list.append(num)
      odd_sum += num
      

# 홀수가 존재하지 않을 경우
if len(number_list) == 0:
  print(-1)
# 홀수가 존재할 경우
else:
  print(odd_sum)
  print(min(number_list))

  