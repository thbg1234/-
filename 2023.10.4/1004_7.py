'''
2023.9.27
석홍신(202195056)
 설명 : 
'''
import random
num1=random.randint(1,100)
num2=random.randint(1,100)
sum=num1+num2
i=1
print(num1,"+",num2,"=",end="")
while i !=0:
    i=int(input())
    if i==sum:
        print("참 잘했어요!")
        continue
    elif i==0:
        print("정답은 ",sum,"입니다")
        continue
    print(num1,"+",num2,"=",end="")

