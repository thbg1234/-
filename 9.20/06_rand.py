'''
    작성일 : 2023년 9월 20일
    작성자 : 석홍신(202195056)


    설명 : 선택문 if~else
           random 을 이용한 가위바위보 게임.
           
           random함수로 생성된 정수를 가지고 게임을 진행합니다.
           0 => 가위
           1 => 바위
           2 => 보
'''
import random  

print(":: 가위 바위 보 게임 시작 ::")

num = random.randrange(3)  

if num == 1 :
    print("가위")
if num == 2 :
    print("바위")
if num == 3 :
    print("보")
    
if num == 1 :
    print("가위")
elif num == 2 :
    print("바위")
else :
    print("보")