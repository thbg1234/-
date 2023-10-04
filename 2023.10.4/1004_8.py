'''
2023.9.27
석홍신(202195056)
 설명 : 
'''

num1=int(input("시자 정수를 입력하세요: "))
num2=int(input("끝 정수를 입력하세요: "))
num11=num1
num22=num2
num111=num1
num222=num2
sum1=0
sum2=0
while num1<=num2:
    sum1=sum1+num1
    num1 +=1
print(num11,"에서",num22,"까지 정수의 합:",sum1)

while num11 <= num22:
    if num11 % 2 == 0:
        sum2 += num11
    num11 += 1
print(num111, "에서", num222, "까지 짝수의 합:", sum2)


