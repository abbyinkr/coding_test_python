'''
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 
최하위 비트(least significant bit, lsb)의 위치는 0이다.

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 10^6)

각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.
'''
# 문제접근
'''
n을 이진수로 변경하여 저장한다. 
1의 위치를 모두 찾는 string 함수를 사용하여 위치가 낮은것부터 출력한다.
'''

# 테스트케이스 수
T = int(input())
1101
for _ in range(T):
  bin = str(format(int(input()), 'b'))

  for i in range(len(bin)):
    # -1 에서 부터 -i-1 거꾸로 출력
    if bin[-i -1] == '1':
      print(i, end=' ')



'''
arr = [1, 2, 3, 4, 5]
# 범위를 거꾸로 
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = ' ')

# 출력을 거꾸로
for i in range(len(s)):
    print(s[-i-1], end = ' ')
'''





  


  
  