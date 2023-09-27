'''
석홍신(202195056)
'''
import random

num1=random.randint(1,100)
num2=random.randint(1,100)

print (num1,"+",num2,"=",end="")

num3=int (input())

if num1+num2==num3:
    print("잘했어요!!")
else:
    print("정답은",num1+num2,"입니다.")