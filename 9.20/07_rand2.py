'''
    작성일 : 2023년 9월 20일
    작성자 : 석홍신(202195056)

    설명 : 선택문 if~else
           random 을 이용한 가위바위보 게임.
           
           random함수로 생성된 정수를 가지고 게임을 진행합니다.
           0 => 가위
           1 => 바위
           2 => 보
           
           두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''
import random   

print(":: 가위 바위 보 게임 시작 ::")

player1 = input("Player1의 이름 : ")
player2 = input("Player2의 이름 : ")

num1 = random.randrange(3)   
num2 = random.randrange(3)   

print(player1, " : ", end='')
if num1 == 1 :
    print("가위")
if num1 == 2 :
    print("바위")
if num1 == 3 :
    print("보")
    
print(player2, " : ", end='')
if num2 == 1 :
    print("가위")
elif num2 == 2 :
    print("바위")
else :
    print("보")
    