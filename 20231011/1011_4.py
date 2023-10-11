'''
2023.9.27
석홍신(202195056)
설명 : 
'''

def cals(num1,num2):
    sum=num1+num2
    minus=num1-num2
    mul=num1*num2
    div=num1/num2
    rest=num1%num2
    return sum,minus,mul,div,rest

num1=int(input("시작 수 입력:")) 
num2=int(input("종료 수 입력:"))

sum,minus,mul,div,rest = cals(num1,num2)
print(f"{num1}+{num2}={sum}")
print(f"{num1}-{num2}={minus}")
print(f"{num1}*{num2}={mul}")
print(f"{num1}/{num2}={div}")
print(f"{num1}%{num2}={rest}")