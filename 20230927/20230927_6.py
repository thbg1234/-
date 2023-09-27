'''2023.9.27
석홍신(202195056)
 설명 :  터틀 그래픽으로 N각형 도형을 그려보자 
            사용자로부터 그리고싶은 도형의 변의 수를 입력 받아
            도형을 그린다.
'''

import turtle as t
t.shape("turtle")

t.penup()
t.goto(-50,-50)
t.pendown()
for i in range(30):
    num = int (t.textinput("도형그리가","몇각형의 도형을 그릴까요"))
 
    for i in range (num):
        t.forward(100)
        t.left(360/num)

t.done()