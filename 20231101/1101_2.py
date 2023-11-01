'''
    작성일 : 2023년 9월 20일
    작성자 :석홍신(202195056)
    
'''
import math

radius= float(input('숫자를 입력하세요:'))

def calCircle(r):
    area = 2*math.pi*r**2
    circum = 2*math.pi*r
    return area,circum

(a,c)=calCircle(radius)
print(str(a),str(c))

circle= calCircle(radius)
print(f"반지름이 {radius}인 원의 넓이는 {circle[0]:.2f}이고, 원의 둘레는 {circle[1]:.2f}이다.")