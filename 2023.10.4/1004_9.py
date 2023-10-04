num1 = int(input("시작 정수를 입력하세요: "))
num2 = int(input("끝 정수를 입력하세요: "))
num11 = min(num1, num2)
num22 = max(num1, num2)
num111 = min(num1, num2)
num222 = max(num1, num2)
sum1 = 0
sum2 = 0
while num11 <= num22:
    sum1 += num11
    num11 += 1
print(num111, "에서", num222, "까지 정수의 합:", sum1)
num11 = min(num1, num2)
while num11 <= num22:
    if num11 % 2 == 0:
        sum2 += num11
    num11 += 1
print(num111, "에서", num222, "까지 짝수의 합:", sum2)