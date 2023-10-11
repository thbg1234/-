'''
2023.9.27
석홍신(202195056)
설명 : 
'''
print("두수 사이의 할 구하기")

def get_sum(start,end):
    sum=0
    if start>end:
        temp= start
        start=end
        end=temp
    for i in range (start,end+1):
        sum+=i
        return sum

num1=int(input("시작 수 입력:"))
num2=int(input("종료 수 입력:"))

sun=get_sum(num1,num2)
print(f"(num1)부터 (num2)까지 합은(sum)")
print(f"")