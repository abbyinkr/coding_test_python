'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
# input() 쓰면 시간초과로 틀림
import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):

  command = sys.stdin.readline()

  push 2 => ['push', '2']
  # command 가 push 로 시작하는 string이라면
  if command.find("push") == 0 :
    n = int(command.split(' ')[1])
    stack.append(n)
     

  elif command.find("pop") == 0:
    if(len(stack)==0):
      print(-1)
    else:
      print(stack[-1])
      stack.pop()
  
  elif command.find("top") == 0 :
    if(len(stack) ==0):
      print(-1)
    else:
      print(stack[-1])
   
  elif command.find("size") ==0 : 
    print(len(stack))
    
  elif command.find("empty") == 0:
    if(len(stack) ==0):
      print(1)
    else:
      print(0)
    
  

#print(stack)