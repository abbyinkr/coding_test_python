'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

입력받은 단어 하나하나를 아스키코드로 변환한다음 97~122 반복문 돌려서 일치하면 처음 등장하는 위치를 저장하고
불일치하면 -1 로 저장한 리스트의 값을 공백으로 구분해서  출력한다.
'''

#소문자 a ~ z 아스키코드 : 97 ~ 122

word = list(input())
word_list = []
for i in word:
  word_list.append(ord(i))
  
#print(word_list)

num_list = []
for i in range(97,123,1):
  num_list.append(i)

#print(num_list)

for i in range(len(num_list)):
  if (num_list[i] in word_list):
    num_list[i] = word_list.index(num_list[i])
  else:
    num_list[i] = -1

for i in num_list:
  print(i, end=" ")

'''
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)))

'''